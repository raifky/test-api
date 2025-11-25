from fastapi import FastAPI, HTTPException
import psycopg2
import pandas as pd

# create FastAPI object
app = FastAPI()

# #Endpoint pintu masuk API 
def getConnection():
    # create connection
    conn = psycopg2.connect(
        dbname="neondb", user="neondb_owner", password="npg_sLfVg8iW4EwO",
        host="ep-steep-water-a102fmjl-pooler.ap-southeast-1.aws.neon.tech",
    )

    return conn


@app.get('/')
def getWelcome():
    return {
        "msg": "sample-fastapi-pg"
    }

#untuk mengambil data dari csv
@app.get('/data')
def getData():
    #untuk membaca data csv
    df = pd.read_csv('data.csv')
#return df juga bisa
    return df.to_dict(orient="records")

@app.get('/data/{lokasi}')
def getData(lokasi: str):
    #untuk membaca data csv
    df = pd.read_csv('data.csv')
    result = df.loc[df.lokasi == lokasi]

    if result.shape[0] == 0:
        raise HTTPException(status_code=404, detail="Data Not Found!")

#return df juga bisa
    return result.to_dict(orient="records")

@app.get('/profile')
async def getProfiles():

    connection = getConnection()

    df = pd.read_sql("""
                select * from profiles;
                """, connection)
    
    return df.to_dict(orient="records")

# @app.get(...)
# async def getProfiles():
#     pass


# @app.get(...)
# async def getProfileById():
#     pass


# @app.post(...)
# async def createProfile():
#     pass


# @app.patch(...)
# async def updateProfile():
#     pass


# @app.delete(...)
# async def deleteProfile():
#     pass

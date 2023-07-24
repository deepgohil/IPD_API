import pymongo
from fastapi import FastAPI, File, UploadFile,status,HTTPException,Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class usearCreateaccount(BaseModel):
    name: str
    phoneno: str 
    location: str
    createDate: str



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

myclient = pymongo.MongoClient("")

#use database named "organisation"
mydb = myclient["appusers"]

#use collection named "developers"
mycol = mydb["details"]

# #a document
# developer = { "name": "deep", "Phone": "+918104680835" }

# #insert a document to the collection
# x = mycol.insert_one(developer)


@app.get("/")
def root():
    return {"message": "Welcome"}


@app.post("/createaccount",status_code=200)
async def upload(usearCreateaccount:usearCreateaccount):
    #a document
    iteam_data=usearCreateaccount.dict()
    #insert a document to the collection
    x = mycol.insert_one(iteam_data)
    return {"message":"account created"}
    
    
import pymongo
from fastapi import FastAPI, File, UploadFile,status,HTTPException,Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


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
    return {"message": "Welcome to the PyMongo tutorial!"}


@app.post("/createaccount",status_code=200)
async def upload(phoneNumber: str = Form(...), name: str = Form(...),location: str = Form(...),accountcreationtime: str = Form(...)):
    #a document
    developer = { "name": name, "Phone": phoneNumber ,"location":location,"accountcreationtime":accountcreationtime}

    #insert a document to the collection
    x = mycol.insert_one(developer)
    return {"message":"account created"}
    
    
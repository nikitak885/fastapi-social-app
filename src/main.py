# main file for the code

from fastapi import FastAPI

app = FastAPI()

app.get("/")
async def root():
    return {"message": "Hello World"}


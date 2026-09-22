from fastapi import FastAPI
from pymongo import AsyncMongoClient
app = FastAPI()
client = AsyncMongoClient("mongodb://localhost:27017/")
db = client["College"]

# select collection
students_collection = db["Students"]

@app.get("/")
async def home():
    return {
        "message": "FastAPI with MongoDB is running",
    }
@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mongodb":"connected", "ping": result["ok"]}
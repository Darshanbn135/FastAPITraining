# This file is the "entry point" of the application.
from fastapi import FastAPI

from app.config import settings
from app.database import ping_database

# Creating FastAPI app instance
app = FastAPI(title=settings.APP_NAME)

# This connection runs once when the server starts. It checks if the MongoDB connection is alive and raises an error if it is not.
@app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("Could not connect to the MongoDB.")
    print(f"[startup] Connected to MongoDB: {settings.APP_NAME}")

# Checks basic health-chek API endpoins & confirms 
# Get / is running & readble. (/ is considered as 'root)
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": f"{settings.APP_NAME} is running."}
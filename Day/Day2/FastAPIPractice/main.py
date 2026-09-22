from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": " Hello World!","number": 63,"is_fun": True}
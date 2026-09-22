from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"page": "Home"}
@app.get("/about")
def about():
    return {"page": "About", "author": "darshan"}
@app.get("/health")
def health():
    return {"status": "okay"}
#post request
@app.post("/create")
def create_something():
    return {"message": "Data created "}

#path parameter
@app.get("/Student/{usn}")
def get_student(usn):
    return {"Result": "Distinction", "USN": usn}

#path parameter with type Hint
@app.get("/Candidate/{rollno}")
def get_candidate(rollno: int):
    return {"Result": "Distinction", "roll No": rollno, "type": str(rollno)}

# Pydantic model
class Item(BaseModel):
    name:str
    price:float
    in_stock: bool = True

@app.post("/items")
def create_item(item:Item):
    return {"received":item, "total_price":item.price*1.18}
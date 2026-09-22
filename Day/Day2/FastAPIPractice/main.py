from fastapi import FastAPI
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
from fastapi import FastAPI , HTTPException
from database import students
from models import Student
from routers.students import router
from fastapi import status
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the student management API!"}

app.include_router(router)



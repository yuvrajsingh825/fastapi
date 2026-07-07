from fastapi import FastAPI , HTTPException
from database import students
from models import Student
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the student management API!"}


@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@app.post("/students")
def create_student(student: Student):
    if student.id in students:
        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )

    students[student.id] = student
    return{
        "message": "Student created successfully",
        "student": student
    }

@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    updated_student.id = student_id
    students[student_id] = updated_student
    return {
        "message": "Student updated successfully",
        "student": updated_student
    }

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail ="Student not found"
        )
    deleted_student = students.pop(student_id)
    return{
        "message":"student deleted sucessfully",
        "student":deleted_student
    }
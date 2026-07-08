#Single Responsibility Principle (SRP)
from fastapi import APIRouter
from models import Student
from database import students
from fastapi import HTTPException
from fastapi import status
from services.student_service import get_all_students
from services.student_service import create_student as create_student_service
from services.student_service import (
    get_student as get_student_service
)
router=APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.get("/", response_model=list[Student])
def get_students():
    return get_all_students()

@router.get("/{student_id}",response_model=Student)
def get_student(student_id: int):
    return get_student_service(student_id)

@router.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    return create_student_service(student)

@router.put("/students/{student_id}")
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

@router.delete("/students/{student_id}")
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

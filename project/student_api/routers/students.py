from fastapi import APIRouter
from models import Student
from database import students
from fastapi import HTTPException

router=APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.get("/", response_model=list[Student])
def get_students():
    return list(students.values())

@router.get("/{student_id}",response_model=Student)
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

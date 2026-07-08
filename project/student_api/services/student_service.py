from database import students
from fastapi import HTTPException
from models import Student


def get_all_students():
    return list(students.values())

def create_student(student: Student):
    if student.id in students:
        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )
    students[student.id] = student
    return student

def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[student_id]

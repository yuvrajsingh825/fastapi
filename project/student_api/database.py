from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(
    DATABASE_URL,
    echo=True
)
class Base(DeclarativeBase):
    pass



try:


    from .models import Student
except ImportError:
    from models import Student

students = {
    1: Student(
        id=1,
        name="Yuvraj",
        age=20,
        course="CSE"
    ),
    2: Student(
        id=2,
        name="Rahul",
        age=21,
        course="AI"
    )
}

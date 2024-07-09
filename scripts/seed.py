import sys
import os

# Додавання шляху до каталогу з файлами models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base, Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random
from datetime import datetime, timedelta

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

def seed():
    groups = [Group(name=faker.unique.word()) for _ in range(3)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(name=faker.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=faker.word(), teacher=random.choice(teachers)) for _ in range(8)]
    session.add_all(subjects)
    session.commit()

    students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)]
    session.add_all(students)
    session.commit()

    grades = []
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.uniform(1, 10),
                    date=faker.date_between(start_date='-1y', end_date='today')
                )
                grades.append(grade)

    session.add_all(grades)
    session.commit()

if __name__ == "__main__":
    seed()
    

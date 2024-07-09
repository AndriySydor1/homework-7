import argparse
import sys
import os

# Додавання шляху до каталогу з файлами models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'models')))

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student, Group, Teacher, Subject, Grade

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher {name} created with ID: {teacher.id}")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(teacher.id, teacher.name)

def update_teacher(id, name):
    teacher = session.query(Teacher).filter(Teacher.id == id).first()
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher {id} updated to {name}")
    else:
        print(f"Teacher with ID {id} not found")

def delete_teacher(id):
    # Видалення всіх пов'язаних записів з таблиці grades
    grades = session.query(Grade).join(Subject).filter(Subject.teacher_id == id).all()
    for grade in grades:
        session.delete(grade)

    # Видалення всіх пов'язаних записів з таблиці subjects
    subjects = session.query(Subject).filter(Subject.teacher_id == id).all()
    for subject in subjects:
        session.delete(subject)
    
    teacher = session.query(Teacher).filter(Teacher.id == id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher {id} deleted")
    else:
        print(f"Teacher with ID {id} not found")

def main():
    parser = argparse.ArgumentParser(description="Manage University Database")
    parser.add_argument('--action', '-a', required=True, choices=['create', 'list', 'update', 'remove'])
    parser.add_argument('--model', '-m', required=True, choices=['Teacher'])
    parser.add_argument('--id', type=int, help='ID of the record')
    parser.add_argument('--name', '-n', help='Name of the record')

    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create' and args.name:
            create_teacher(args.name)
        elif args.action == 'list':
            list_teachers()
        elif args.action == 'update' and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == 'remove' and args.id:
            delete_teacher(args.id)
        else:
            print("Invalid arguments for the specified action")

if __name__ == "__main__":
    main()
    
    
    
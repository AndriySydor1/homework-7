from my_select import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10
)

def main():
    print("Top 5 students by average grade:")
    print(select_1())

    print("Student with highest average grade in a specific subject (subject_id=1):")
    print(select_2(1))

    print("Average grade in groups for a specific subject (subject_id=1):")
    print(select_3(1))

    print("Average grade across all grades:")
    print(select_4())

    print("Courses taught by a specific teacher (teacher_id=1):")
    print(select_5(1))

    print("List of students in a specific group (group_id=1):")
    print(select_6(1))

    print("Grades of students in a specific group (group_id=1) for a specific subject (subject_id=1):")
    print(select_7(1, 1))

    print("Average grade given by a specific teacher (teacher_id=1):")
    print(select_8(1))

    print("Courses attended by a specific student (student_id=1):")
    print(select_9(1))

    print("Courses taught by a specific teacher (teacher_id=1) to a specific student (student_id=1):")
    print(select_10(1, 1))

if __name__ == "__main__":
    main()
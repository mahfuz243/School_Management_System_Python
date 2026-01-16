
from student import Student
from course import Course

file_name = "students.txt"


def save_student(student):
    with open(file_name, "a") as file:
        file.write(str(student) + "\n")


def show_all_students():
    try:
        with open(file_name, "r") as file:
            print("\n--- All Students Record ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student data found!")



if __name__ == "__main__":
    while True:
        print("\n1. Enroll Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student Name: ")
            roll = input("Roll Number: ")
            password = input("Password: ")

            student = Student(name, roll, password)

            course_count = int(input("How many courses to enroll: "))
            for _ in range(course_count):
                course_name = input("Course Name: ")
                course = Course(course_name)
                student.enroll_course(course)

            save_student(student)
            print("Student enrolled successfully!")

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            print("Thank you for using this Student Management System!")
            break

        else:
            print("Invalid choice!")

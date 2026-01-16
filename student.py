class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def get_password(self):
        return self.__password

    def __str__(self):
        course_names = ", ".join([str(course) for course in self.courses])
        return f"Name: {self.name}, Roll: {self.roll}, Courses: {course_names}"




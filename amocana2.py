class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def show_info(self):
        print(f"Name: {self.name} \nStudent ID: {self.student_id} \nCourses:")
        for course in self.courses:
            print("     -" + course)


student1 = Student("Nika", "001", ["Math", "Science"])
student1.show_info()

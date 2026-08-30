# Create a class 'Student' with name, age, grade attributes
# and a method to display student info

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def student_info(self):
        print(f"Student name | {self.name}\nStduent age is | {self.age}\nStudent grade | {self.grade}")

Student_A = Student("Niranjan", 32, "98%")
Student_B = Student("vinutha", 26, "99%")
print("**********************************")
Student_A.student_info()
print("**********************************")
Student_B.student_info()
print("**********************************")

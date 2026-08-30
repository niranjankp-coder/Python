# Single Inheritence

class student:
    def m1(self):
        print("m1 method")

class student_2(student):
    def m2(self):
        print("m2 method")

std = student_2()
std.m1()
std.m2()

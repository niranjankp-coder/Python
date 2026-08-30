class school_A:
    def A_school_info(self):
        print("Located at Bangalore")

class school_B(school_A):
    def B_school_info(self):
        print("Located at Mysore")

class school_C(school_B):
    def C_school_info(self):
        print("Located at Mandya")

school = school_C()
school.A_school_info()
school.B_school_info()
school.C_school_info()

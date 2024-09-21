class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone
        self.allstudents = []

    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nID-number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}\n"

    def addStudent(self, var):
        self.allstudents.append(var)
        print(f"Added student {var.name} to the list.")
'''
    def printAllStudentInfo(self):
        print("\n==========All Student's Info==========\n")
        for _ in self.allstudents:
            print(_)
        print("============Nothing Follows===========")
'''

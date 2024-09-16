class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone
        self.allstudents = []

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID-number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}\n"
    
    def menu(self):
        m = int(input("\n[1] View Student Info\n[2] Search for Student ID-number\n[3] Add Student\n[4] Exit\nEnter your choice: "))
        if m == 1:
            w = int(input("\n[1] View all students' info\n[2] View an individual student info\nEnter your choice: "))
            if w == 1: self.printAllStudentInfo(); self.menu()
            elif w == 2: self.searchStudent(); self.menu()
        elif m == 2: pass
        elif m == 3: self.addStudent(); self.menu()
        else: exit()

    def searchStudent(self):
        s = input("\nEnter student's name: ")
        for _ in self.allstudents:
            if _.name == s:
                print("\n==========Student's Info==========\n")
                print(_)
                print("==========Nothing Follows=========")

    def addStudent(self):
        n, a, i, e, p = input("\nEnter Name: "), int(input("Enter Age: ")), input("Enter ID-number: "), input("Enter Email: "), input("Enter Phone: ")
        var = StudentInfo(n, a, i, e, p)
        self.allstudents.append(var)
        print(f"\nAdded student {var.name} to the list.")

    def printAllStudentInfo(self):
        print("\n==========All Student's Info==========\n")
        for _ in self.allstudents:
            print(_)
        print("============Nothing Follows===========")

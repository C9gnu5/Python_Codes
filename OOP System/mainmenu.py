class MainMenu:
    def __init__(self, data):
        self.data = data

    def menu(self):
        m = int(input("""
Welcome Admin ! Please choose any of the following
[1] Check your information
[2] Search for someone's information
[3] Register a new student
[4] Print all student in the InfoSys
[5] Exit the system
Enter your choice: """))
        if m == 1: pass
        elif m == 2: self.searchStudent(); self.menu()
        elif m == 3: self.registerStudent(); self.menu()
        elif m == 4: self.data.printAllStudentInfo(); self.menu()
        elif m == 5: print("============System Exiting============"); exit()
        else: print("Choice invalid!"); self.menu()

    def searchStudent(self):
        while True:
            id = input("\nEnter student ID Number: ")
            print(self.data.search_student(id))
            again = input("\n Do you want to search again? (Y/N) ")
            if again.lower() != "y":
                print("============Exiting Search============")
                break

    def registerStudent(self):
        n, a, i, o, p = input("\nEnter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        

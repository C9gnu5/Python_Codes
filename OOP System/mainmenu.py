from student import StudentInfo
import os

class MainMenu:
    def __init__(self, student_data, finder):
        self.student_data = student_data
        self.finder = finder

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
        elif m == 2: self.searchStudent()
        elif m == 3: self.registerStudent()
        elif m == 4: self.finder.printAllStudentInfo(); self.backToMenu()
        elif m == 5: os.system('cls' if os.name == 'nt' else 'clear'); exit()
        else: print("\n!!CHOICE INVALID!!"); self.menu()

    def backToMenu(self):
        back = input("\nPress 'Y' to go back to Main Menu or any key to quit program: ")
        if back.lower() != 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.menu()
    
    def searchStudent(self):
        while True:
            os.system('cls')
            id = input("\nEnter student ID Number: ")
            print(self.finder.search_student(id))
            again = input("\nDo you want to search again? (Y/N) ")
            if again.lower() != "y":
                self.backToMenu()
                # os.system('cls')
                # break

    def registerStudent(self):
        os.system('cls')
        print("\n============STUDENT REGISTRY============")
        n, a, i, o, p = input("\nEnter Name: "), input("Enter Age: "), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone: ")
        print("\n===========STUDENT REGISTERED===========\n")
        s = StudentInfo(n, a, i, o, p)
        self.student_data.addStudent(s)
        self.backToMenu()

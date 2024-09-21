import os

class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def search_student(self, id):
        for student in self.student_data.allstudents:
            if student.idnum == id:
                print("\n============Student's Info============\n")
                print(student) 
                return "\n============Nothing Follows==========="
        return f"\nSTUDENT WITH ID NUMBER {id} COULD NOT BE FOUND!"
            
    def printAllStudentInfo(self):
        os.system('cls')
        print("\n============ALL STUDENT'S INFO============\n")
        for student in self.student_data.allstudents:
            print(student)
        print("\n==============NOTHING FOLLOWS=============")
        
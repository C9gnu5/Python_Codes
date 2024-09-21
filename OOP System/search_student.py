class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def search_student(self, id):
        for student in self.student_data.allstudents:
            if student.idnum == id:
                print("\n============Student's Info============\n")
                print(student) 
                return "============Nothing Follows==========="
        return f"\nStudent with ID Number {id} could not be found!"
            
    def printAllStudentInfo(self):
        print("\n============All Student's Info============\n")
        for student in self.student_data.allstudents:
            print(student)
        print("==============Nothing Follows=============")
class students:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def calculate_average_grade(self):
            return sum(self.grades) / len(self.grades) #summing all the grades then dividing it to the length of the grades list
    
    def compare_students(self):
        s1 = input("Enter first student's name: ")
        if s1 in students_list: #checking if student name is already registered
            s2 = input("Enter student's name to compare to: ")
            if s2 in students_list: #checking if student name is already registered
                if students_list[s1].calculate_average_grade() < students_list[s2].calculate_average_grade():
                    print(-1, f"{students_list[s1].name}'s average grade is lower than {students_list[s2].name}'s.")
                elif students_list[s1].calculate_average_grade() == students_list[s2].calculate_average_grade():
                    print(0, f"{students_list[s1].name}'s average grade is equal to {students_list[s2].name}'s.")
                else:
                    print(1, f"{students_list[s1].name}'s average grade is greater than {students_list[s2].name}'s.")
            else:
                print("Student name not found. Please register the student first!")
                main()
        else:
            print("Student name not found. Please register the student first!")
            main()
        

def add_student():
    sn = input("Enter student's name: ")
    grades = []
    if sn not in students_list:
        s = students(sn, grades)
        students_list[sn] = s
    else:
        print("Student already registered!")
        
def add_grades():
    global sn #globalizing sn variable so ags() function can use the variable
    sn = input("Enter student's name to be graded: ")
    if sn in students_list: #checking if student name is already registered
        ags() #invoking funtion for the actual appending of grades
    else:
        print("Student name not found. Please register the student first!")
        r = input("Register a student? [y] or press any key to return to main menu ")
        if r in ["y", "Y"]: 
            add_student() #if you want to add student without returning to main menu
        else:
            main()
        
def ags(): #function for the actual appending of grades
    g = int(input("Enter the grade of the student: "))
    students_list[sn].grades.append(g) #appending or adding the grade to the student's list of grades
    h = input("Enter another grade[y] or change student to add grade to[c] or return to main menu[m]? ")
    if h in ["y", "Y"]: #if another grade is to be inputted
        ags() #to loop back into entering a grade
    elif h in ["c", "C"]: #for changing the student to be graded
        add_grades()
    elif h in ["m", "M"]: #for returning to main menu
        main()
    else:
        print("Error")

def show_grade():
    sn = input("Enter student's name: ")
    if sn in students_list: #checking if student name is already registered
        print(f"{students_list[sn].name}'s grades are {students_list[sn].grades}") #fetching and printing the student's list of grades
    else:
        print("Student name not found. Please register the student first!")

def ranking():
    rank = {}
    for name, student in students_list.items(): #iterating each key value in students_list
        rank[name] = student.calculate_average_grade() #storing the name as key and average grade as value into the rank storage
    sorted_rank = sorted(rank.items(), key=lambda x: x[1], reverse=True) #sorted the items by value in descending order
    for i, (name, grade) in enumerate(sorted_rank, start=1): #iterating and indexing the sorted rank
        print(f"{i}. {name}: {grade}")
        
def main():
    m = input("""
[1]Add Student
[2]Add Grades
[3]View Grades
[4]Calculate Student Average Grade
[5]Compare Student's Grades
[6]View Student Ranking
""")
    if m == "1":
        add_student()
        main()
    elif m == "2":
        add_grades()
    elif m == "3":
        show_grade()
        main()
    elif m == "4":
        sn = input("Enter student's name: ")
        if sn in students_list:
           print(students_list[sn].calculate_average_grade())
           main()
        else:
            print("Student name not found. Please register the student first!")
            main()
    elif m == "5":
        students.compare_students()
        main()
    elif m == "6":
        ranking()
        main()
    else:
        print("Error")
        exit()
        
    
students_list = {} #storage for the students object

main()

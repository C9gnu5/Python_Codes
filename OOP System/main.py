from student import StudentInfo
from search_student import SearchStudent
from mainmenu import MainMenu

stu = StudentInfo("name", "age", "idnum", "email", "phone")
search = SearchStudent(stu)
me = MainMenu(search)

stud = [["Markus", "22", "2023-2-00700", "email@g.co", "Eyaw"],
        ["Joe", "20", "2023-2-00309", "joemama@qpal.co", "Wag pre"],
        ["Joriz", "19", "2023-2-00465", "liampo@qpal.co", "Eeeeyyyy"]]

for i in stud:
    st = StudentInfo(*i)
    stu.addStudent(st)

print(me.menu())

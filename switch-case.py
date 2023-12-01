def case01():
    ct = int(input("Enter call duration:"))
    tc = input("Enter time code:[1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        return ct * 3.00
    elif tc == "2":
        return ct * 8.00
    else:
        return "Invalid"


def case02():
    ct = int(input("Enter call duration:"))
    tc = input("Enter time code:[1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        return ct * 4.00
    elif tc == "2":
        return ct * 10.00
    else:
        return "Invalid"


def case03():
    ct = int(input("Enter call duration:"))
    tc = input("Enter time code:[1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        return ct * 2.00
    elif tc == "2":
        return ct * 5.00
    else:
        return "Invalid"


def case04():
    ct = int(input("Enter call duration:"))
    tc = input("Enter time code:[1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        return ct * 9.00
    elif tc == "2":
        return ct * 12.00
    else:
        return "Invalid"


def case05():
    ct = int(input("Enter call duration:"))
    tc = input("Enter time code:[1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        return ct * 20.00
    elif tc == "2":
        return ct * 25.00
    else:
        return "Invalid"


def error():
    return "Invalid"


cd = input("""
Call destination              ON-PEAK  OFF-PEAK
[1]To same network             P3.00    P8.00
[2]To other network            P4.00    P10.00
[3]To a landline               P2.00    P5.00
[4]National direct call        P9.00    P12.00
[5]International direct call   P20.00   P25.00
\nChoose call destination:""")

cdopt = {
    "1": case01,
    "2": case02,
    "3": case03,
    "4": case04,
    "5": case05
}

print(cdopt.get(cd, error)())

cd = input("""
Call destination              ON-PEAK  OFF-PEAK
[1]To same network             P3.00    P8.00
[2]To other network            P4.00    P10.00
[3]To a landline               P2.00    P5.00
[4]National direct call        P9.00    P12.00
[5]International direct call   P20.00   P25.00
\nChoose call destination:""")

match cd:
    case "1":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        match tc:
            case "1":
                print("P"+str(3.00*ct))
            case "2":
                print("P"+str(8.00*ct))
            case _:
                print("Invalid time code!")
    case "2":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        match tc:
            case "1":
                print("P"+str(4.00*ct))
            case "2":
                print("P"+str(10.00*ct))
            case _:
                print("Invalid time code!")
    case "3":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        match tc:
            case "1":
                print("P"+str(2.00*ct))
            case "2":
                print("P"+str(5.00*ct))
            case _:
                print("Invalid time code!")
    case "4":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        match tc:
            case "1":
                print("P"+str(9.00*ct))
            case "2":
                print("P"+str(12.00*ct))
            case _:
                print("Invalid time code!")
    case "5":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        match tc:
            case "1":
                print("P"+str(20.00*ct))
            case "2":
                print("P"+str(25.00*ct))
            case _:
                print("Invalid time code!")
    case _:
        print("Invalid call destination!")

cd = input("""Choose call destination\t\tON-PEAK\tOFF-PEAK
[1]To same network\t\tP3.00\tP8.00
[2]To other network\t\tP4.00\tP10.00
[3]To a landline\t\tP2.00\tP5.00
[4]National direct call\t\tP9.00\tP12.00
[5]International direct call\tP20.00\tP25.00\n:""")

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

def main():
    cd = input("""
Call destination              ON-PEAK  OFF-PEAK
[1]To same network             P3.00    P8.00
[2]To other network            P4.00    P10.00
[3]To a landline               P2.00    P5.00
[4]National direct call        P9.00    P12.00
[5]International direct call   P20.00   P25.00
\nChoose call destination:""")
    if cd == "1":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        if tc == "1":
            print(ct*3.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        elif tc == "2":
            print(ct*8.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        else:
            print("Invalid")
    elif cd == "2":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        if tc == "1":
            print(ct*4.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        elif tc == "2":
            print(ct*10.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        else:
            print("Invalid")
    elif cd == "3":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        if tc == "1":
            print(ct*2.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        elif tc == "2":
            print(ct*5.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        else:
            print("Invalid")
    elif cd == "4":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        if tc == "1":
            print(ct*9.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        elif tc == "2":
            print(ct*12.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        else:
            print("Invalid")
    elif cd == "5":
        ct = float(input("Enter call duration:"))
        tc = input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
        if tc == "1":
            print(ct*20.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        elif tc == "2":
            print(ct*25.00, "Pesos")
            re = input("Would you like to call again?[1]Yes or [2]No\n")
            if re == "1":
                main()
            elif re == "2":
                exit()
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")


main()

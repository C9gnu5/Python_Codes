cd=input("""Choose call destination\t\tON-PEAK\tOFF-PEAK
         \n[1]To same network\t\tP3.00\tP8.00
         \n[2]To other network\t\tP4.00\tP10.00
         \n[3]To a landline\t\tP2.00\tP5.00
         \n[4]National direct call\t\tP9.00\tP12.00
         \n[5]International direct call\tP20.00\tP25.00\n:""")
if cd == "1":
    ct=float(input("Enter call duration:"))
    tc=input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        print(ct*3.00, "Pesos")
    elif tc == "2":
        print(ct*8.00, "Pesos")
    else:
        print("Invalid")
elif cd == "2":
    ct=float(input("Enter call duration:"))
    tc=input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        print(ct*4.00, "Pesos")
    elif tc == "2":
        print(ct*10.00, "Pesos")
    else:
        print("Invalid")
elif cd == "3":
    ct=float(input("Enter call duration:"))
    tc=input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        print(ct*2.00, "Pesos")
    elif tc == "2":
        print(ct*5.00, "Pesos")
    else:
        print("Invalid")
elif cd == "4":
    ct=float(input("Enter call duration:"))
    tc=input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        print(ct*9.00, "Pesos")
    elif tc == "2":
        print(ct*12.00, "Pesos")
    else:
        print("Invalid")
elif cd == "5":
    ct=float(input("Enter call duration:"))
    tc=input("\nEnter time code: [1]ON-PEAK or [2]OFF-PEAK\n")
    if tc == "1":
        print(ct*20.00, "Pesos")
    elif tc == "2":
        print(ct*25.00, "Pesos")
    else:
        print("Invalid")
else:
    print("Invalid")

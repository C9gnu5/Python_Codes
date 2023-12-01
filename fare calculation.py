pt = input("""
Passenger Type    Discount    Fare
[1]Regular          None      P9.00
[2]Student          20%       P7.2
[3]Senior Citizen   25%       P6.75
[4]PWD              30%       P6.3
\nChoose passenger type:""")

mf = 9.00
dis20 = 9/100*20
dis25 = 9/100*25
dis30 = 9/100*30

if pt == "1":
    km = int(input("\nEnter travel distance(KM):"))
    if km <= 4:
        print("P"+str(mf))
    elif km > 4:
        print("P"+str((km-4)*1.50+mf))
elif pt == "2":
    km = int(input("\nEnter travel distance(KM):"))
    if km <= 4:
        print("P"+str(mf-dis20))
    elif km > 4:
        print("P"+str((km-4)*1.50+mf-dis20))
elif pt == "3":
    km = int(input("\nEnter travel distance(KM):"))
    if km <= 4:
        print("P"+str(mf-dis25))
    elif km > 4:
        print("P"+str((km-4)*1.50+mf-dis25))
elif pt == "4":
    km = int(input("\nEnter travel distance(KM):"))
    if km <= 4:
        print("P"+str(mf-dis30))
    elif km > 4:
        print("P"+str((km-4)*1.50+mf-dis30))
else:
    print("Invalid")

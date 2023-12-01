#1. Display the place values of a 4 digit number without using string functions, lists, and libraries.

n = int(input("Enter a 4 Digit Number: "))

print("Thousands:", n // 1000)
print("Hundreds:", n % 1000 // 100)
print("Tens:", n % 100 // 10)
print("Ones:", n % 10 // 1)


print("")
#2. Write a complete python program using a loop to implement the output below when the output is run.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

for i in range(10):
    for j in range(i+1):
        print("*", end="")
    print()


print("")
#3. Write a complete python program that will assign the elements 2, 12, 14, 8 and 10 to the array "arrTest".
#The program must display the elements of the array as well as the location of element 8 in the array.

arrTest = [2, 12, 14, 8, 10]

for i in range(len(arrTest)):
    for element in arrTest:
        if element == 8:
            break
            
print("The elements of arrTest are " + ' '.join(map(str, arrTest)) + ".")
print("Element " + str(element), "is in index", str(i)+".")

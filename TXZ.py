def letter_t(n):
    t = ""
    if n % 2 == 0:
        n += 1
    for i in range(n):
        for j in range(n):
            if i == 0 or j == n // 2:
                t += "*"
            else:
                t += " "
        t += "\n"
    return t


def letter_x(n):
    x = ""
    if n % 2 == 0:
        n += 1
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                x += "*"
            else:
                x += " "
        x += "\n"
    return x


def letter_z(n):
    z = ""
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n - i:
                z += "*"
            else:
                z += " "
        z += "\n"
    return z


lt = input('Choose a letter, [1]"T", [2]"X", [3]"Z": ')
match lt:
    case "1":
        t = int(input('\nEnter number for letter "T": '))
        print(letter_t(t))
    case "2":
        x = int(input('\nEnter number for letter "X": '))
        print(letter_x(x))
    case "3":
        z = int(input('\nEnter number for letter "Z": '))
        print(letter_z(z))
    case _:
        print("Invalid")

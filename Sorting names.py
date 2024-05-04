def names_entry():
    names = []
    x = True
    while x:
        try:
            n = input("Enter a name to add to the list or enter 'x' to stop: ")
            if n in {"x", "X"}:
                x = False
            elif n.isspace():
                raise ValueError("Blank Input, Please Enter a Name!")
            else:
                names.append(n)
        except ValueError as e:
            print("Error: ", e)
    return names

def sorter(target_list, sort_type="alphabetical"):
    if sort_type == "alphabetical":
        return sorted(target_list)
    elif sort_type == "length":
        return sorted(target_list, key = len)
    elif sort_type == "vowels_number":
        #for descending order: reverse = True
        return sorted(target_list, key = lambda v: sum(1 for _ in v if _.lower() in {"a", "e", "i", "o", "u"}))

name = names_entry()
print("Default list:", name)
print("Alphabetical Order:", sorter(name))
print("Length Order:", sorter(name, "length"))
print("Number of Vowels Order:", sorter(name, "vowels_number"))

      
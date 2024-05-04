from random import randint

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, (len(list)-i-1)):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def descend_selection(list):
    for i in range(len(list)):
        max_i = i
        for j in range(i+1, len(list)):
            if list[j] > list[max_i]:
                max_i = j
        list[i], list[max_i] = list[max_i], list[i]
    return list

l = []
for i in range(20):
    l.append(randint(1, 100))

print("Original list:", l)
print("Bubble Sort:", bubble_sort(l))
print("Selection Sort:", descend_selection(l))


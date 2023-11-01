# Write a menu driven program to demonstrate use of list in python:
# 1. put even and odd elements into two different lists
# 2. merge and sort the two list
# 3. update fist element with X value and delete the middle element of the list
# 4. find max and min elements from the list
# 5. add N names into the existing number list and check if word python is present in the list

import math
odd = []
even = []
numbers = []
names = []
while (True):
    print('1. enter even and odd numbers in lists')
    print('2. merge and sort the list and display')
    print('3. update the first element of list and delete the middle element')
    print('4. min and max of the list')
    print('5. add names and find python')
    print("6. quit")
    choice = int(input('enter the choice: '))
    if (choice == 1):
        n = int(input("enter the number of elements: "))
        i = 0
        while (i<n):
            i = i+1
            numb = int(input('enter the number: '))
            if (numb%2 == 0):
                even.append(numb)
            else:
                odd.append(numb)
        print("even list:", even)
        print("odd list:",odd)
    elif (choice == 2):
        numbers = even
        numbers.extend(odd)
        numbers.sort()
        print("merged list is: ", numbers)
    elif (choice == 3):
        new = int(input("enter the element you want to enter:"))
        numbers[0] = new
        print(numbers)
        length = len(numbers)
        # print(math.ceil(length/2))
        numbers.pop(math.ceil(length/2 - 1))
        print(numbers)
    elif (choice == 4):
        print("Min is: ", min(numbers))
        print("Max is: ",max(numbers))
    elif (choice == 5):
        n = int(input("enter the number of elements: "))
        i = 0
        while (i<n):
            i = i+1
            name = input('enter the name: ')
            names.append(name)

        print("name list:",names)
        for i in names:
            if i == 'python':
                print("python is there as a name")
    elif (choice == 6):
        break
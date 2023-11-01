# Implement python programs to explore files and directories 
# 1. python program to count number of lines, words and characters in a file
# 2. python program to display files available in the current directory

import os
def menu():
    print("\n///MENU///")
    print("1. To read content of one file and write it to another file")
    print("2. To append data at the end of existing file")
    print("3. To count number of lines, words and characters in a file")
    print("4. To display files in current directory")
    print("5. Exit")
    return(int(input("\nEnter your choice: ")))
c=0
while c!=5:
    c = menu()
    if c==3:
        c=l=w=0
        fname = input("\nEnter the file name: ")
        f = open(fname+".txt", "r")
        for x in f:
            print(x)
            words = x.split()
            l+=1
            w+=len(words)
            c+=len(x)
        print("\nNo. of lines = ", l)
        print("\nNo. of words = ", w)
        print("\nNo. of characters = ", c)
        f.close()
    elif c==4:
        print("\nThe files in current directory are:-\n")
        for files in os.walk('.'):
            for x in range(0, len(files[2])):
                print(files[2][x])
    elif c!=5:
        print("\nIncorrect choice")




# write a menu driven python program to check for number and string 
# palindrome

print("1.number palingrome")
print("2.string palingrome")
choice = int(input("enter the choice: "))
fact = 1

# number palindrome
if (choice == 1):
    s = input("enter the pallindrome: ")
    opposite = s[::-1]
    if s==opposite:
        print("the input is a palindrome")
    else:
        print("the input is not a palindrome")

# string palindrome
elif(choice==2):
    s = input("enter the pallindrome: ")
    opposite = s[::-1]
    if s==opposite:
        print("the input is a palindrome")
    else:
        print("the input is not a palindrome")

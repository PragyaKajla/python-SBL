# Write a python program to swap two numbers and check if the first number is positive or 
# negative or zero

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
temp = b
b = a
a = temp
print("the number are swapped: a =",a,"b =",b)
if (a>0):
    print("the first number positive")
elif (a<0):
    print("the first number is negative")
else:
    print("the first number is zero")


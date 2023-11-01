# write a program to demonstrate exception handlind in python

n = int(input("enter the numerator: "))
d = int(input("enter the denominator: "))

try:
    c = n/d
    print('the quotient is: ', c)
except ZeroDivisionError:
    print("cannto enter 0 in the denominator")


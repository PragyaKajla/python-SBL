# write a python program to demonstrate inheritance in python

class Person:
    def __init__(self, id, name):
        self.ID = id
        self.name = name
    def display(self):
        print("\nID = ", self.ID)
        print("\nName = ", self.name)

class Student(Person):
    def __init__(self, x, y, id, name):
        super().__init__(id, name)
        self.sub1 = x
        self.sub2 = y
    def display(self):
        print("\nStudent ID = ", self.ID)
        print("Student Name = ", self.name)
        print("Marks in subject 1 = ", self.sub1)
        print("Marks in subject 2 = ", self.sub2)

class Result(Student):
    def __init__(self, id, name, x, y):
        super().__init__(x, y, id, name)
    def total(self):
        sum1 = self.sub1 + self.sub2
        print("\nWe have, Total Marks = ", sum1, "\n")

print("Enter the student details:-")
id = input("\nEnter Student ID: ")
name = input("\nEnter Student Name: ")
m1 = int(input("\nEnter marks in first subject: "))
m2 = int(input("\nEnter marks in second subject: "))

obj = Result(id, name, m1, m2)
obj.display()
obj.total()
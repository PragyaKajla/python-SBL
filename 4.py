# write a program to demonstrate classes, objects and constructor

# Program to demonstrate classes and objects
class Dog:
    animal = 'dog'
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

class Cat:
    animal = 'cat'
    def __init__(self, color, age):
        self.color = color
        self.age = age
 
Echo = Cat( "white", 5)
Zera = Dog("Mallinois", "brown-black", 2)
 
print('Echo details:')
print('Echo is a', Echo.animal)
print('Color: ', Echo.color)
print('Age: ', Echo.age)


 
print('\nZera details:')
print('Zera is a', Zera.animal)
print('Breed: ', Zera.breed)
print('Color: ', Zera.color)
print('Age: ', Zera.age)
 
print("\nAccessing class variable using class name")
print(Dog.animal)
print(Cat.animal)
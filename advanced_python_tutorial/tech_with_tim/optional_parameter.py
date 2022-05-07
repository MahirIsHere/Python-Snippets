def func(x):
    return pow(x, 2)


call = func(5)
print(call)

"""multiple parameters"""


def newfun(x, y):
    print(x * y)


call = newfun("Mahir", 10)

# class
class Pet:
    def __init__(self, animal, breed, name):
        self.animal = animal
        self.breed = breed
        self.name = name

    def printname(self):
        print(self.animal, self.breed, self.name)


pet1 = Pet("Fish", "gold fish", "rich man")
pet2 = Pet("Dog", "black labrador", "Captain")
pet1.printname()
pet2.printname()

# static vs class method
# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("Mahir", 22)
person2 = Person.fromBirthYear("Rahman", 1998)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

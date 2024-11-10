"""Inheritance is a mechanism that allows us to define the common behaviour in one class 
and then inherit them in other classes."""


class Animal:  # Parent class
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent Base class
# Mammal: Child, Sub class


class Mammal(Animal):

    def walk(self):  # we define a method.
        print("walk")


class Fish(Animal):
    def eat(self):
        print("eat")

    def swim(self):
        print("walk")


cat = Mammal()  # an instance of the class Mammal.
dog = Mammal()
japanesefish = Fish()

cat.eat()
dog.walk()
print(cat.age)

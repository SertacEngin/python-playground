"""The __init__ method is a special method in Python, known as constructor.
It is called automatically when an instance (object) of a class is created.
It's used to initialize the instance's attributes (variables specific to each object)."""


class Dog:
    # The __init__ method initializes the instance attributes
    def __init__(self, name, breed):
        self.name = name  # Instance attribute 'name'
        self.breed = breed  # Instance attribute 'breed'

    # A regular method that uses instance attributes
    def bark(self):
        print(f"{self.name} says: Woof!")

    # Another regular method
    def display_info(self):
        return f"Dog's Name: {self.name}, Breed: {self.breed}"


# Creating an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Using regular methods
my_dog.bark()  # Output: Buddy says: Woof!
# Output: Dog's Name: Buddy, Breed: Golden Retriever
print(my_dog.display_info())

"""__init__ method is automatically called when my_dog = Dog("Buddy", "Golden Retriever") is executed.
It sets the name and breed attributes for the instance.
"""

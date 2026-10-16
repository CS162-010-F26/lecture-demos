# This is a Python module. Basically, any .py file is a Python module.

# Global scope is also called module scope.

# Specifically, this is the dog module. Here I'll define a Dog
# class, and some functions that operate on Dog objects.

class Dog:
    breed: str
    owner: str
    age: int

def create_dog(breed: str, owner: str, age: int) -> Dog:
    result = Dog()
    result.breed = breed
    result.owner = owner
    result.age = age
    return result

def print_dog(the_dog: Dog) -> None:
    print(the_dog.breed)
    print(the_dog.owner)
    print(the_dog.age)

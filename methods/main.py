from typing import Self

# Classes can also have behaviors. That's to say, it's possible to
# create "can-do" relationships. You do this with methods.
# Basically, a method is a function that exists inside an instance
# of a class.
class Dog:
    breed: str
    owner: str
    age: int

    # A constructor (an initializer) is a special method that's automatically
    # called, implicitly, the moment an object of the given class is
    # created (i.e., constructed). The purpose of a constructor is to
    # "set up", or initialize, the object.
    # A constructor's name must be __init__. Its return type must be None.
    def __init__(self, breed: str, owner: str, age: int) -> None:
        self.breed = breed
        self.owner = owner
        self.age = age

    def bark(self) -> None:
        print('Bark! Bark!')

    def print(self) -> None:
        print(self.breed)
        print(self.owner)
        print(self.age)
        self.bark()

    def greet(self, other_dog: Self) -> None:
        print(f'Hello, {other_dog.owner}\'s dog')


def main() -> None:
    # clifford = create_dog('Big Red', 'Elizabeth', 50)
    clifford = Dog('Big Red', 'Elizabeth', 50)

    clifford.print()

    scooby = Dog('Great Dane', 'Shaggy', 1000)

    scooby.print()

    scooby.greet(clifford)

    # In Python, the word "object" is often used to refer
    # to any class instance. Basically, any piece of data.

    # In traditional "object-oriented programming", an object
    # is a class instance, where the class provides data, behaviors
    # that operate on that data, and identity.





if __name__ == '__main__':
    main()

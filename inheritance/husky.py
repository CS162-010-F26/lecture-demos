from dog import Dog
from sled import Sled

# This is known as inheritance.
# You write class DerivedClass(BaseClass).
# This tells the interpreter that the Husky class (derived class)
# inherits from the Dog class (base class).

# Sometimes, you'll hear the terminology child / parent classes,
# or sub / super classes.
# Subclass == child class == derived class.
# Superclass == parent class == base class.

# I will typically use derived / base class.

# When a derived class inherits from a base class, everything that is defined
# in the base class is effectively implicitly defined in the derived class
# as well.

# Loosely, you can think of inheritance relationships as "is-a" relationships.
# That is to say, a Husky IS A Dog.
class Husky(Dog):
    _energy: int

    def __init__(self) -> None:
        self._energy = 100

    # We can introduce new attributes and methods in our Husky class.
    # This is known as extension.
    def pull_sled(self, sled: Sled) -> None:
        if self._energy <= 0:
            return

        sled.distance_pulled += 5
        self._energy -= 5

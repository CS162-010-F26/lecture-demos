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

    def __init__(self, owner: str, name: str, age: int) -> None:
        # These attributes are private to the Dog class.
        # self._name = name # Violation of encapsulation. DONT do this.
        # self._age = age # Same as above.

        # The Husky class SORT OF has two constructors.
        # It turns out that you can call EITHER ONE of those constructors
        # at will. If you want to call the DOG class constructor (the base
        # class constructor), you have to use a special explicit syntax.
        # The super keyword:

        # The super() function, when used like so in a method of a derived
        # class, essentially reinterprets self (the calling object) as an
        # object of the base class.
        super().__init__(owner, name, age)

        self._energy = 100

    # We can introduce new attributes and methods in our Husky class.
    # This is known as extension.
    def pull_sled(self, sled: Sled) -> None:
        if self._energy <= 0:
            return

        sled.distance_pulled += 5
        self._energy -= 5

    # This method is known as an override.
    # An override is a method in a derived class with the exact same
    # header as another method that was inherited from an ancestor.
    def vocalize(self) -> None:
        print('Awooo!')

        # Let's say, here, I want to call the husky's inherited Dog-class
        # vocalize() method
        super().vocalize()

from dog import Dog
from husky import Husky
from sled import Sled

def main() -> None:
    spot = Dog('Mahatma', 'Spot', 3)
    spot.vocalize()

    # Now that the Husky class has an explicitly defined constructor,
    # this will attempt to call THAT constructor, instead of the Dog
    # class constructor.
    delilah = Husky('Janette', 'Delilah', 4)

    # If you have an object with two or more "versions" (overrides) of the
    # same method, then by default, when you attempt to call the method on
    # the object, it will prefer the version that is from the "most derived"
    # class in the inheritance hierarchy.
    delilah.vocalize() # This calls Husky class's vocalize() method on delilah

    # It is possible to call delilah's Dog-class vocalize() method.
    # If you want to do this from outside the Husky-class methods:
    super(Husky, delilah).vocalize()

    santas_sleigh = Sled()
    santas_sleigh.distance_pulled = 0

    delilah.pull_sled(santas_sleigh)
    print(santas_sleigh.distance_pulled)

    # spot.pull_sled(santas_sleigh)

if __name__ == '__main__':
    main()

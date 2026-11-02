from dog import Dog
from husky import Husky
from sled import Sled

def main() -> None:
    spot = Dog('Spot', 3)
    spot.bark()

    # Now that the Husky class has an explicitly defined constructor,
    # this will attempt to call THAT constructor, instead of the Dog
    # class constructor.
    delilah = Husky('Delilah', 4)
    delilah.bark()

    santas_sleigh = Sled()
    santas_sleigh.distance_pulled = 0

    delilah.pull_sled(santas_sleigh)
    print(santas_sleigh.distance_pulled)

    # spot.pull_sled(santas_sleigh)

if __name__ == '__main__':
    main()

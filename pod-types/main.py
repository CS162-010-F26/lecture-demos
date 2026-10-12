# Define a Car POD type here.
# Typically, custom data types (e.g., classes, POD types, etc)
#  are named with PascalCase.

# A class is simply some kind of data type.

# A POD type is a plain-old-data type. Basically it's a type of data
# comprised entirely of smaller pieces of data within it.
# Sometimes, POD types are also referred to as record types, or passive
# data structures.
class Car:
    # Class body goes here.
    # For a POD type, because a POD type just stores data, the class body
    # typically just contains definitions of fields. A field is a smaller
    # piece of data that exists within a larger piece of data.
    year: int
    make: str
    model: str

def main() -> None:
    # int, float, bool, str. These things are primitive types.

    # But you can create more complex types. Composite types.

    # ex. Person, Car, Truck, Player, Zombie. Not provided by Python
    # or the standard library. YOU have to define these types. We typically
    # define them at global scope.



if __name__ == '__main__':
    main()

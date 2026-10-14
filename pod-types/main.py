class SteeringWheel:
    diameter_inches: float

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

    # You'll commonly hear the "has-a" relationship terminology.
    year: int
    make: str
    model: str
    steering_wheel: SteeringWheel

def print_steering_wheel(the_steering_wheel: SteeringWheel) -> None:
    print(f'Steering Wheel Diameter: {the_steering_wheel.diameter_inches} inches')

def print_car(the_car: Car) -> None:
    print(f'Make: {the_car.make}')
    print(f'Model: {the_car.model}')
    print(f'Year: {the_car.year}')
    print_steering_wheel(the_car.steering_wheel)
    # the_car.make = 'Jeep' # This does, actually, modify the make field
    # of the car that was passed in as an argument


def create_car(
        make: str,
        model: str,
        year: int,
        steering_wheel: SteeringWheel) -> Car:
    result = Car()
    result.year = year
    result.make = make
    result.model = model
    result.steering_wheel = steering_wheel
    return result


def main() -> None:
    # int, float, bool, str. These things are primitive types.

    # But you can create more complex types. Composite types.

    # ex. Person, Car, Truck, Player, Zombie. Not provided by Python
    # or the standard library. YOU have to define these types. We typically
    # define them at global scope.

    # In Python, an object is loosely any value
    ford_taurus_steering_wheel = SteeringWheel()
    ford_taurus_steering_wheel.diameter_inches = 12
    ford_taurus = create_car(
        'Ford',
        'Taurus',
        2001,
        ford_taurus_steering_wheel
    )
    #ford_taurus = Car()
    #ford_taurus.year = 2001
    #ford_taurus.make = 'Ford'
    #ford_taurus.model = 'Taurus'

    toyota_fourrunner_steering_wheel = SteeringWheel()
    toyota_fourrunner_steering_wheel.diameter_inches = 13
    toyota_fourrunner = create_car(
        'Toyota',
        'Four Runner',
        2026,
        toyota_fourrunner_steering_wheel
    )
    #toyota_fourrunner = Car()
    #toyota_fourrunner.year = 2026
    #toyota_fourrunner.make = 'Toyota'
    #toyota_fourrunner.model = 'Four Runner'

    print_car(ford_taurus)
    print(ford_taurus.make) # Prints Jeep

    print()

    print_car(toyota_fourrunner)



if __name__ == '__main__':
    main()

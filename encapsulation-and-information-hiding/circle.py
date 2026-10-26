# Encapsulation does two things for us:
# 1. Helps control coupling
# 2. Helps establish class invariants

# A class invariant is a property that is guaranteed to always hold
# for all objects of a given class.

class Circle:
    _radius: float

    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError(f'Circle radius cannot be negative. Got {radius}')
        self._radius = radius

    def get_radius(self) -> float:
        return self._radius

    def set_radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError(f'Circle radius cannot be negative. Got {radius}')
        self._radius = radius


# You shouldn't reflexively create getters and setters for just any and
# all private attributes.

# Getters and setters often have brittle interfaces.

# The goal  of encapsulation is: when designing a class, ask yourself:
# What are the fundamental responsibilities of objects of this class?
# What are the operations that objects of this class are responsible for?
# Create interfaces that align with those responsibilities. Then, figure
# out the implementation details under the hood.

def main() -> None:
    c = Circle(5)
    # c._radius = -1
    c.set_radius(3)
    print(3.14 * c.get_radius() * c.get_radius())

    # What's the worst case scenario here?
    # In the worst case, this is a subtle logic error.
    # It might propagate.

if __name__ == '__main__':
    main()

from math import sqrt

class Pair[T1, T2]:
    field1: T1
    field2: T2

    def __init__(self, arg1: T1, arg2: T2) -> None:
        self.field1 = arg1
        self.field2 = arg2

def quadratic_formula(a: float, b: float, c: float) -> Pair[float, float]:
    return Pair(
        (-b - sqrt(b ** 2 - 4*a*c)) / (2*a),
        (-b + sqrt(b ** 2 - 4*a*c)) / (2*a)
    )

def main() -> None:
    roots = quadratic_formula(3, 2, 1)
    print(roots.field1)
    print(roots.field2)

if __name__ == '__main__':
    main()

# A tuple is a generalization of pairs, but potentially to more than 2
# fields. A tuple is simply a group of N fields, of N types.

# There is a built-in tuple data structure in Python

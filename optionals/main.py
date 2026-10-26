def f(x: int | str) -> None:
    print(x * 3.5)

def main() -> None:
    # Optionals

    # But first, union types
    # int | str is a union type.
    # typing.Union[int, str]
    x: int | str = 'hello'
    print(type(x)) # class <int>
    x = 5
    print(type(x)) # class <str>
    print(x)

    # From Mypy's perspective, an operation on a union-typed variable
    # is only supported if it's supported in turn by all of the types
    # involved in the union.
    f(x)

    # Generally speaking, the above statement makes union types fairly
    # weak.

    # This is why, generally, union types are often avoided.

    # However, with one exception: There is a category of union types
    # referred to as "optionals". Optionals are very commonly used.

    # An optional is a union type where one of the types is None
    player_1_pokemon: Pokemon | None = None

    # More or less, the purpose of an optional is to represent data that,
    # at a given point in time, may or may not exist / be known.


if __name__ == '__main__':
    main()

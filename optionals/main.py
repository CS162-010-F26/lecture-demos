#def f(x: int | str) -> None:
#    print(x * 3.5)

class Pokemon:
    _hp: int

    def __init__(self) -> None:
        self._hp = 5

    def get_hp(self) -> int:
        return self._hp

def g(some_pokemon: Pokemon) -> int:
    return some_pokemon.get_hp()

class City:
    _name: str
    _population: int | None

    def __init__(self, name: str, population: int | None) -> None:
        self._name = name
        self._population = population

    def get_population(self) -> int | None:
        return self._population

    def double_the_population(self) -> None:
        if self._population is not None:
            self._population = self._population * 2

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
    # f(x)

    # Generally speaking, the above statement makes union types fairly
    # weak.

    # This is why, generally, union types are often avoided.

    # However, with one exception: There is a category of union types
    # referred to as "optionals". Optionals are very commonly used.

    # An optional is a union type where one of the types is None
    player_1_pokemon: Pokemon | None = Pokemon()

    # More or less, the purpose of an optional is to represent data that,
    # at a given point in time, may or may not exist / be known.
    
    # "is" and "is not" are both operators.
    # They are NOT the same thing as == and !=.

    player_1_pokemon = None

    if player_1_pokemon is not None:
        print(g(player_1_pokemon))



if __name__ == '__main__':
    main()

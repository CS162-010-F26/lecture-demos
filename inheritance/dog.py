from pet import Pet

class Dog(Pet):
    _name: str
    _age: int

    def __init__(self, owner: str, name: str, age: int) -> None:
        # self._owner = owner # Violation of encapsulation
        super().__init__(owner)
        self._name = name
        self._age = age

    def vocalize(self) -> None:
        print(f"Bark! Bark! My name is {self._name}, and I'm "
            f"{self._age} years old")

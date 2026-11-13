from typing import override

from item import Item

class Car(Item):
    make: str
    model: str
    year: int

    @override
    def print(self) -> None:
        super().print()
        print(f'\tMake: {self.make}')
        print(f'\tModel: {self.model}')
        print(f'\tYear: {self.year}')

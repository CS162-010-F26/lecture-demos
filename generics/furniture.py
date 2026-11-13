from typing import override

from item import Item

class Furniture(Item):
    name: str

    @override
    def print(self) -> None:
        super().print()
        print(f'\tName: {self.name}')

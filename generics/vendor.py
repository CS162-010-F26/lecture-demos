from item import Item

# T is a generic type parameter.
# A parameter in general is just a placeholder.
# Generic type parameters are specifeically placeholders
# for NAMES OF TYPES.

# Using generic type parameters is a strategy known as
# parametric polymorphism because we have parameterized
# a type, allowing us to use various type names in place
# of that type parameter.

# Vendor is now a generic class. It is no longer a regular class.
# A generic class is simply a class with one or more
# generic type parameters within its definition.
class Vendor[T: Item]:
    _inventory: list[T]
    _money: float

    def __init__(self) -> None:
        self._inventory = []
        self._money = 0

    def add_item_to_stock(self, item: T) -> None:
        self._inventory.append(item)

    def sell_item(self, index: int) -> None:
        self._money += self._inventory[index].price
        del self._inventory[index]

    def print(self) -> None:
        print(f'Money: {self._money}')
        print('Inventory:')
        for item in self._inventory:
            item.print()

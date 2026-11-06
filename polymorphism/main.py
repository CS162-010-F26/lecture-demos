from player import Player
from zombie import Zombie
from vampire import Vampire
from monster import Monster

def do_turn(
        player: Player,
        monsters: list[Monster]) -> None:
    for m in monsters:
        m.attack_player(player)
    
    player.print()

def main() -> None:
    player = Player()

    # Our maintainability issue: We have a seperate list for every derived
    # class. The solution to this issue is polymorphism.

    # Upcasting: Upcasting is when you type-cast an object of a given
    # class into one of its ancestor classes. Typically, in Python,
    # we upcast "implicitly".

    # Implicit typecasting is when you store an object of one type
    # in a variable annotated as a different, but compatible, type
    # my_float: float = 1

    # You can implicitly upcast.
    # my_zombie = Zombie()
    # my_monster: Monster = my_zombie

    # Polymorphism means "many forms". It refers to a case where
    # you have a variable whose actual type may be one of many
    # possibilities.

    # Specifically, polymorphism achieved via implicit upcasting
    # is known as subtype polymorphism.

    monsters: list[Monster] = []

    # 5 zombies
    for _ in range(5):
        monsters.append(Zombie())
    
    # 3 vampires
    for _ in range(3):
        monsters.append(Vampire())

    # Game loop
    while player.is_alive():
        do_turn(player, monsters)

if __name__ == '__main__':
    main()

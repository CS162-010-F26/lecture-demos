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

    # Abstract classes CANNOT be instantiated.
    # i.e., I cannot construct plain old Monster objects anymore.

    # x = Monster() # CANT DO THIS
    # monsters.append(x) # CANT DO THIS

    # Game loop
    while player.is_alive():
        do_turn(player, monsters)


    # In many programming languages, a variable has two types:
    # A static type is the type of the variable as annotated in the code,
    # or inferred by static analysis tools. m's static type is monster.
    # A dynamic type is the type of object that the variable actually
    # refers to at a given point in time while the program is running.
    # m's dynamic type is zombie
    # monster* m = new zombie()

    # Dynamic types can change. Static types do not.
    # m = new vampire()

    # Method call binding: This is the action of the computer associating
    # a method call with a definition for that method. There are different
    # times that a computer might do this. A computer might do this
    # during, say, compilation / at program startup. (ahead of time).
    # We call this early binding or static binding. An alternative is
    # late binding / dynamic binding, where the computer makes such decisions
    # on the fly, when actually executing the method call.

    # Static binding must be doable by analyzing just the source code.
    # A static type of a variable is a type that can be dtermined by
    # just analyzing the source code.
    # Therefore, static binding relies entirely on static types.

    # Dynamic binding, on the other hand, relies on dynamic types.

    # Subtype polymorphism inherently requires dynamic binding.

    # However, it's slower than static binding.

    # In Python, all function calls are always bound dynamically. In many
    # other languages, you must opt into dynamic binding to get subtype
    # polymorphism to work.

if __name__ == '__main__':
    main()

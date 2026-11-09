from abc import ABC, abstractmethod

from player import Player

# abc (and ABC) stand for abstract base class.


# In order to make a class an abstract class,
# you must first make it inherit from ABC.


class Monster(ABC):
    # We need this method to make Mypy happy, but its
    # implementation is sort of useless. It is possible
    # to keep this method in existence without implementing
    # it. That's known as an abstract method.

    # By decorating attack_player with the @abstractmethod
    # decorator, it is now an abstract method.
    @abstractmethod
    def attack_player(self, player: Player) -> None:
        # Abstract methods do not have to be fully defined.
        # That is, I can leave this method body empty now.
        pass

        # In fact, an abstract method is basically MEANT to be
        # empty, at least in the base class

        # The purpose of an abstract method is to provide
        # an interface without implementation. That is to say,
        # monsters CAN attack the player, but exactly HOW they do that
        # shall be decided by the derived classes.

        # Abstract methods should only be defined in classes that inherit
        # from ABC (in abstract classes). That is, only abstract classes
        # should be allowed to have abstract methods.

# Formally, an abstract class is a class with one or more unimplemented
# abstract methods.

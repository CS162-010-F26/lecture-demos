from monster import Monster
from player import Player

class Vampire(Monster):
    _strength: int

    def __init__(self) -> None:
        self._strength = 1

    def attack_player(self, player: Player) -> None:
        print('Vampire attacks player')
        # The vampire sucks the player's blood, damaging them
        # by an amount equal to the vampire's current strength,
        # and increasing the vampire's strength by 1, up to a max
        # of 5
        player.take_damage(self._strength)

        if self._strength < 5:
            self._strength += 1

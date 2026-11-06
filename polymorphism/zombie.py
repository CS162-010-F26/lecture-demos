from monster import Monster
from player import Player

class Zombie(Monster):
    _sanity: int

    def __init__(self) -> None:
        self._sanity = 3

    def attack_player(self, player: Player) -> None:
        print('Zombie attacks player')
        if self._sanity > 0:
            # The zombie is still sane. They will not damage
            # the player. But they will lose one sanity.
            self._sanity -= 1
            return

        # The zombie is insane, so they damage the player
        player.take_damage(2)

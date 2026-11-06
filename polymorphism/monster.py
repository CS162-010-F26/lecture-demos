from player import Player

class Monster:
    # We need this method to make Mypy happy, but its
    # implementation is sort of useless. It is possible
    # to keep this method in existence without implementing
    # it. That's known as an abstract method.
    def attack_player(self, player: Player) -> None:
        print('Argh! I\'m a monster! I attack you!')

from src import *


def main():
    game: Game = Game(_playerAmt=1, _startingCardAmt=3)
    player = game.players[0]
    player.setHand([
        (None, 1),
        (None, 2),
        (None, 3)
    ])
    player.swapCard((None, 4))
    print(player.hand)


if __name__ == "__main__":
    main()
    exit(0)

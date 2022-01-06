from sys import argv, stdout
from src import *


def _env():
    pass


def main():
    game: Game = Game()
    player: int = 0

    game.setupRound()

    while True:
        if len(game.discardStack) > 0:
            stdout.write("Draw from Discard Stack?")
            stdout.write(f"Top of stack: {game.discardStack[-1]}")
            stdout.flush()
            uIp = input("[y|N]")
        else:
            uIp = "y"

        if uIp in '':
            uIp = "-1"

        if uIp in "yY":
            card: tuple = game.getCard()
        else:
            card: tuple = game.getDiscardStackTop()

        discard: tuple = game.players[player].swapCard(card)
        game.discardStack.append(card)

        player = (player + 1) % game.playerAmt


if __name__ == "__main__":
    # _env()
    main()
    exit(0)

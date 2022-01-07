from sys import argv, stdout
from platform import system
from subprocess import run
from src import *


def _getMinPointIdx(points: list[int]) -> (int|False):
    if len(points) != len(set(points)):
        return False
    mn: int = min(points)
    return points.index(mn)


def _cls() -> None:
    compProc = None
    match system():
        case "Windows":
            compProc = run(["cls"], shell=True)
        case ("Linux"|"Mac"):
            compProc = run(["clear"], shell=True)
        case _:
            raise SystemError()
    if compProc.returncode:
        raise ChildProcessError()
    return


def main():
    game: Game = Game()

    while True:
        for player in game.players
            _cls()
            uIp: str = ''

            game.setupRound()

            if game.discardStack:
                stdout.write("Will you draw from the norm stack,\nor the discard stack?\n")
                stdout.flush()
                uIp = input("[y|n]> ")

            if uIp and uIp in "yY":
                card: tuple = game.getDiscardStackTop()
            else:
                card: tuple = game.getCard()

            card = player.swapCard(card)

            game.discardStack.append(card)

        points: list[int] = game.calcPoints()
        minPointIndex: int = _getMinPointIdx(points)

        winner: bool = game.players[minPointIndex].decroHandSize()

        if winner:
            wPlay = game.players[minPointIndex]
            break

    stdout.write(f"The player {wPlay} is the winner!\n")
    stdout.write("Please tell them they are an idiot for winnig\n")
    stdout.flush()


if __name__ == "__main__":
    # _env()
    main()
    exit(0)

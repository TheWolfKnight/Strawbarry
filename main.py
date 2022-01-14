#!/usr/bin/env python3

from sys import argv, stdout
from platform import system
from subprocess import run
from typing import Union
from src import *


def _getMinPointIdx(points: list[int]) -> Union[int, bool]:
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
    game: Game = Game(_playerAmt=2)

    while True:
        game.setupRound()

        while game.playingCards:
            for player in game.players:
                uIp = ""
                if game.discardStack:
                    print("Do you want to draw from the deck or discard stack?")
                    uIp = input("[DECK|disc] ")

                if uIp in ('', "DECK", "deck"):
                    card: tuple[str] = game.getCard()

                    print("Will you pass {}?".format(
                        ", ".join(card)
                    ))
                    uIp = input("[y|N] ")
                    if uIp not in "nN":
                        game.discardStack.append(card)
                        continue
                else:
                    card: tuple[str] = game.getDiscardStackTop()

                card = player.swapCard(card)
                game.discardStack.append(card)

        points: list[int] = game.calcPoints()
        minPointIndex: int = _getMinPointIdx(points)

        winner: bool = game.players[minPointIndex].decroHandSize()

        if winner:
            wPlay = game.players[minPointIndex]
            break

    print(f"The player {wPlay} is the winner!\n")
    print("Please tell them they are an idiot for winnig\n")
    
if __name__ == "__main__":
    # _env()
    main()
    exit(0)

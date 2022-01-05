from src import *


def main():
    game: Game = Game()
    game.setupRound()
    points: list[int] = game.calcPoints()
    print(points)
    return

if __name__ == "__main__":
    main()
    exit(0)

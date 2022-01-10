#!/usr/bin/env python3


if __name__ == "__main__":
    exit(1)


class Hand(object):
    def __init__(self, playerName: str, _handSize: int=5):
        self.playerName = playerName
        self.handSize: int = _handSize
        self.hand: list[tuple] = []
        self.hiddenCard: tuple = None

    def setHand(self, hand: list[tuple]) -> None:
        self.hand = hand
        return

    def decroHandSize(self) -> bool:
        if not (self.handSize - 1):
            return True
        self.handSize -= 1
        return False

    def setHiddenCard(self, card: tuple) -> None:
        self.hiddenCard = card
        return

    def swapCard(self, card: tuple) -> tuple:
        currCard: tuple = card

        for idx, card in enumerate(self.hand):
            print("Would you like to swap: {', '.join(card)}\nWith: {', '.join(currCard)}")
            uIp = input("[y|N]> ")
            if uIp in '':
                uIp = '-1'

            if uIp in 'yY':
                pass

            currCard self.hand[idx] = self.hand[idx], currCard

        return currCard

    def __repr__(self) -> str:
        return f"Nx{self.playerName};{"Cx".join()};Hx{}"

    def __str__(self) -> str:
        return f"{self.playerName}"

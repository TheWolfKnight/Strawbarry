
if __name__ == "__main__":
    exit(1)


# from python self
from random import randrange as rdrange
from typing import Iterable

# from locale
from .hand import Hand


class Game(object):
    POINTMAP: dict[str, int] = {
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": 10,
        "Nine": 9,
        "Eigth": 8,
        "Seven": 7,
        "Six": 6,
        "Five": 5,
        "Four": 4,
        "Three": 3,
        "Two": 2,
        "Ace": 1
    }

    CARDSHEET: list[tuple] = [('Hearts', 'King'), ('Hearts', 'Queen'), ('Hearts', 'Jack'), ('Hearts', 'Ten'), ('Hearts', 'Nine'), ('Hearts', 'Eigth'),
                              ('Hearts', 'Seven'), ('Hearts', 'Six'), ('Hearts', 'Five'), ('Hearts', 'Four'), ('Hearts', 'Three'), ('Hearts', 'Two'),
                              ('Hearts', 'Ace'), ('Dimonds', 'King'), ('Dimonds', 'Queen'), ('Dimonds', 'Jack'), ('Dimonds', 'Ten'), ('Dimonds', 'Nine'),
                              ('Dimonds', 'Eigth'), ('Dimonds', 'Seven'), ('Dimonds', 'Six'), ('Dimonds', 'Five'), ('Dimonds', 'Four'), ('Dimonds', 'Three'),
                              ('Dimonds', 'Two'), ('Dimonds', 'Ace'), ('Clubs', 'King'), ('Clubs', 'Queen'), ('Clubs', 'Jack'), ('Clubs', 'Ten'), ('Clubs', 'Nine'),
                              ('Clubs', 'Eigth'), ('Clubs', 'Seven'), ('Clubs', 'Six'), ('Clubs', 'Five'), ('Clubs', 'Four'), ('Clubs', 'Three'), ('Clubs', 'Two'),
                              ('Clubs', 'Ace'), ('Spades', 'King'), ('Spades', 'Queen'), ('Spades', 'Jack'), ('Spades', 'Ten'), ('Spades', 'Nine'), ('Spades', 'Eigth'),
                              ('Spades', 'Seven'), ('Spades', 'Six'), ('Spades', 'Five'), ('Spades', 'Four'), ('Spades', 'Three'), ('Spades', 'Two'), ('Spades', 'Ace')]

    def __init__(self, _playerAmt: int=4, _startingCardAmt: int=5):
        ###
        # self vars from __ini__ params
        self.playerAmt = _playerAmt
        self.startingCardAmt = _startingCardAmt
        ###

        ###
        # self vars from internal
        self.playingCards = self.CARDSHEET
        self.players: list[Hand] = [ Hand(str(i+1), self.startingCardAmt) for i in range(self.playerAmt) ]
        self.nullCard = next(self.nextNullCard())
        self.discardStack: list[tuple] = []
        ###

    def nextNullCard(self) -> str:
        cards: Iterable = self.POINTMAP.keys()
        while True:
            for card in cards:
                yield card

    def getCard(self) -> tuple:
        return self.playingCards.pop(rdrange(0, len(self.playingCards)))

    def setupRound(self) -> None:
        self.playingCards = self.CARDSHEET
        for player in self.players:
            tmp: list[tuple] = [ self.playingCards.pop(rdrange(0, len(self.playingCards))) for _ in range(player.handSize) ]
            player.setHand(tmp)
            player.setHiddenCard(self.playingCards.pop(rdrange(0, len(self.playingCards))))
        return

    def calcPoints(self) -> list[int]:
        r: list[int] = [ None for _ in range(self.playerAmt) ]
        for idx, player in enumerate(self.players):
            tmp: int = 0
            for _, card in player.hand:
                if card == self.nullCard:
                    continue
                tmp += self.POINTMAP[card]
            if not player.hiddenCard[1] == self.nullCard:
                tmp += self.POINTMAP[player.hiddenCard[1]]
            r[idx] = tmp
        return r


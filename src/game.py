
if __name__ == "__main__":
    exit(1)


from itertools import product
from .hand import Hand


class Game(object):
    POINTMAP: dict[str, int] = {
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "Ten": "clear",
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

    def __init__(self, playerAmt: int=4):
        self.playerAmt = playerAmt
        self.playingCards = self.CARDSHEET
        self.players: list[Hand] = []

    def _generateCards(self) -> list[tuple]:
        return list(product(self.suitList, self.pointMap.keys()))

    def setupGame(self) -> None:
        for _ in self.playerAmt:
            pass
        return


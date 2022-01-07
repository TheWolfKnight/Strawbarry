
if __name__ == "__main__":
    exit(1)


from sys import stdout


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
        idx: int = 0
        currCard: tuple = card
        start: bool = True
        while True:

            if idx == len(self.hand)-1:
                currCard, self.hand[idx] = self.hand[idx], currCard
                stdout.write("You swaped:\n")
                stdout.write(f"Hand[{idx+1}]: {self.hand[idx][0]}/{self.hand[idx][1]}, Hold: {currCard[0]}/{currCard[1]}\n")
                stdout.flush()
                return currCard

            stdout.write("Do you want to swap your cards?\n")
            stdout.write(f"Hand[{idx+1}]: {self.hand[idx][0]}/{self.hand[idx][1]}, Hold: {currCard[0]}/{currCard[1]}\n")
            stdout.flush()
            uIp: chr = input("[y|p|N]> ") if start else input("[y|N]> ")

            if uIp in '':
                uIp = "-1"

            if uIp in "pP" and start:
                return currCard

            currCard, self.hand[idx] = self.hand[idx], currCard

            if uIp in 'yY':
                stdout.write("You swaped:\n")
                stdout.write(f"Hand[{idx+1}] {self.hand[idx][0]}/{self.hand[idx][1]}, Hold: {currCard[0]}/{currCard[1]}\n")
                return currCard

            start = False
            idx += 1

    def __repr__(self) -> str:
        return f""

    def __str__(self) -> str:
        return f"{self.playerName}"

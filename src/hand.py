
if __name__ == "__main__":
    exit(1)


from sys import stdout


class Hand(object):
    def __init__(self, handSize: int=5):
        self.handSize: int = handSize
        self.hand: list[tuple] = []
        self.hiddenCard: tuple = None

    def setHand(self, hand: list[tuple]) -> None:
        self.hand = hand
        return

    def setHandSize(self, size: int) -> None:
        self.handSize = size
        return

    def setHiddenCard(self, card: tuple) -> None:
        self.hiddenCard = card
        return

    def swapCard(self, card: tuple) -> tuple:
        idx: int = 0
        currCard: tuple = card
        while True:

            if idx == len(self.hand):
                currCard, self.hand[idx] = currCard, self.hand[idx]
                return currCard

            stdout.write("Do you want to swap your cards?\n")
            stdout.write(f"Hand: {self.hand[idx][0]}/{self.hand[idx][1]}, Hold: {currCard[0]}/{currCard[1]}\n")
            stdout.flush()
            uIp: chr = input("[y|N]> ")

            currCard, self.hand[idx] = self.hand[idx], currCard

            if uIp in ['y','Y']:
                return currCard

            idx += 1

#!/usr/bin/env python3

if __name__ == "__main__":
    exit(1)


from enum import Enum


class Values(Enum):
    A = "Ace"
    K = "King"
    Q = "Queen"
    J = "Jack"
    10 = "Ten"
    9 = "Nine"
    8 = "Eigth"
    7 = "Seven"
    6 = "Six"
    5 = "Five"
    4 = "Four"
    3 = "Three"
    2 = "Two"


class Suits(Enum):
    H = "Hearts"
    D = "Dimonds"
    S = "Spaeds"
    C = "Clubs"

import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
}
import random
class exception100(Exception):
    pass

class exception0(Exception):
    pass

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    
    def __repr__(self):
        return f"{self.letter}:{self.value}"
LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 8,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "Ñ": 8,
                 "O": 1,
                 "P": 3,
                 "Q": 5,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "X":  8,
                 "Y":  4,
                 "Z": 10,
                 "LL": 8,
                 "CH": 5,
                 "RR": 8,
                 "#": 0,
}
LETTER_QUANTITY = {"A": 12,
                 "B": 2,
                 "C": 4,
                 "D": 5,
                 "E": 12,
                 "F": 1,
                 "G": 2,
                 "H": 2,
                 "I": 6,
                 "J": 1,
                 "L": 4,
                 "M": 2,
                 "N": 5,
                 "Ñ": 1,
                 "O": 9,
                 "P": 2,
                 "Q": 1,
                 "R": 5,
                 "S": 6,
                 "T": 4,
                 "U": 5,
                 "V": 1,
                 "X":  1,
                 "Y":  1,
                 "Z": 1,
                 "LL": 1,
                 "CH": 1,
                 "RR": 1,
                 "#": 2,
}
class BagTiles:
    
    def __init__(self):
        self.bag = []
        self.initialize_bag()
        

    def add_to_bag(self, tile, quantity):
        if len(self.bag) + quantity > 100:
            raise exception0("no se pueden agregar mas fichas.")
        if len(self.bag) + quantity < 0:
            raise exception0("no pueden haber menos fichas en la bolsa.")
        for i in range(quantity):
            self.bag.append(tile)


    def initialize_bag(self):
        global LETTER_VALUES, LETTER_QUANTITY

        for letter, value in LETTER_VALUES.items():
            quantity = LETTER_QUANTITY.get(letter, 0)
            self.add_to_bag(Tile(letter, value), quantity)
        random.shuffle(self.bag)    
        
    

    def take(self, count):
        if len(self.bag) < count:
            raise exception100("intentando tomar mas fichas de las disponibles")
        tiles = []
        for _ in range(count):
            tiles.append(self.bag.pop())
        return tiles

    def put(self, tiles):
        self.bag.extend(tiles)





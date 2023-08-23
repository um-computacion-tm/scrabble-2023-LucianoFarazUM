import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

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







class BagTiles:
    def __init__(self):
          
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        
        global LETTER_VALUES
        self.add_to_bag(Tile("A", LETTER_VALUES), 12)
        self.add_to_bag(Tile("B", LETTER_VALUES), 2)
        self.add_to_bag(Tile("C", LETTER_VALUES), 4)
        self.add_to_bag(Tile("D", LETTER_VALUES), 5)
        self.add_to_bag(Tile("E", LETTER_VALUES), 12)
        self.add_to_bag(Tile("F", LETTER_VALUES), 1)
        self.add_to_bag(Tile("G", LETTER_VALUES), 2)
        self.add_to_bag(Tile("H", LETTER_VALUES), 2)
        self.add_to_bag(Tile("I", LETTER_VALUES), 6)
        self.add_to_bag(Tile("J", LETTER_VALUES), 1)
        self.add_to_bag(Tile("L", LETTER_VALUES), 4)
        self.add_to_bag(Tile("LL",LETTER_VALUES), 1)
        self.add_to_bag(Tile("M", LETTER_VALUES), 2)
        self.add_to_bag(Tile("N", LETTER_VALUES), 5)
        self.add_to_bag(Tile("O", LETTER_VALUES), 9)
        self.add_to_bag(Tile("P", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("R", LETTER_VALUES), 5)
        self.add_to_bag(Tile("S", LETTER_VALUES), 6)
        self.add_to_bag(Tile("T", LETTER_VALUES), 4)
        self.add_to_bag(Tile("U", LETTER_VALUES), 5)
        self.add_to_bag(Tile("V", LETTER_VALUES), 1)
        self.add_to_bag(Tile("X", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Y", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Z", LETTER_VALUES), 1)
        self.add_to_bag(Tile("CH", LETTER_VALUES),1)
        self.add_to_bag(Tile("RR", LETTER_VALUES),2)
        self.add_to_bag(Tile("Ñ", LETTER_VALUES) ,2)
        self.add_to_bag(Tile("#", LETTER_VALUES), 2)
        
        random.shuffle(self.bag)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.bag.pop())
        return tiles
    def put(self, tiles):
        self.bag.extend(tiles)

# class BagTiles:

#     def __init__(self):
#         self.bag = []
#         self.initialize_bag()

    
#         self.bag = []
#         self.initialize_bag

       
#     def initialize_bag(self):
#         for letter, value in LETTER_VALUES.items():
#             self.add_to_bag(Tile(letter, value), self.get_initial_quantity(letter))

#         random.shuffle(self.bag)

    
#         self.add_to_bag(Tile(letter, value), self.get_initial_quantity(letter))

#         random.shuffle

#         self.add_to_bag(Tile)

#     def add_to_bag(self, tile, quantity):
#         for _ in range(quantity):
#             self.bag.append(tile)
#     def get_initial_quantity(self, letter):
#         return LETTER_VALUES.get(letter, 0)
#     def take(self, count):
#         tiles = []
#         for _ in range(count):
#             tiles.append(self.bag.pop())
    
#             tiles.append(self.bag.pop())
   
#         return tiles
# # Crear la bolsa de fichas
# bag = BagTiles()

# # Barajar las fichas
# random.shuffle(bag.bag)

# # Repartir 7 fichas
# hand = bag.take(
# 7)
# for tile in hand:
#     print(f"Letter: {tile.letter}, Value: {tile.value}")
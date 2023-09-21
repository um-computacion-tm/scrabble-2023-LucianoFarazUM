class Player:
    def __init__(self, bag_tiles):
        self.bag_tiles = bag_tiles
        self.score = 0
        self.tiles = []

    def add_letter(self, letter):
        self.tiles.append(letter)

    def get_letters(self):
        return self.tiles


    def get_score(self):
        return self.score
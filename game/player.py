
class Player:
    def __init__(self, bag_tiles, nickname="nombre/apodo"):
        self.bag_tiles = bag_tiles
        self.score = 0
        self.rack = self.bag_tiles.take(7)  
        self.nickname = nickname
        
    def handle_wildcard(self, word_list, wildcard, new_letter, rack_copy):
        for i, letter in enumerate(word_list):
            if letter == wildcard:
                for tile in rack_copy:
                    if tile.letter == wildcard:
                        word_list[i] = new_letter
                        tile.letter = new_letter
                        break

    def set_wildcard(self, word):
        new_letter = input("Ingrese la letra del comodin: ")
        word_list = list(word)
        rack_copy = self.rack.copy()

        self.handle_wildcard(word_list, "#", new_letter, rack_copy)
        self.handle_wildcard(word_list, "@", new_letter, rack_copy)

        modified_word = "".join(word_list)
        self.rack = rack_copy
        return modified_word
        
    def renew_rack(self,matching_tiles):
        for tile in matching_tiles:
            if tile in self.rack:
                self.rack.remove(tile)
        self.fill_rack() 

    def set_nickname(self):
        self.nickname = input('Ingrese su nombre/apodo: ')
        
    def display_rack(self):
        rack_strings = [str(tile) for tile in self.rack]  
        print("Sus fichas son: " + ", ".join(rack_strings))

    def is_letter_in_rack(self, word):
        player_letters = {}
        for tile in self.rack:
            letter = tile.letter
            player_letters[letter] = player_letters.get(letter, 0) + 1
        
        for letter in word:
            if player_letters.get(letter, 0) > 0:
                player_letters[letter] -= 1
            else:
                raise KeyError(f"Falta la letra '{letter}' para formar la palabra '{word}'.")
        
        return True

    def fill_rack(self):
        new_tiles=self.bag_tiles.take(7-len(self.rack))
        self.rack+=new_tiles

    def add_letters(self, letters):
        self.rack.extend(letters)

    def get_score(self):        
        return self.score
    
    def update_score(self, points):
        self.get_score
        self.score += points

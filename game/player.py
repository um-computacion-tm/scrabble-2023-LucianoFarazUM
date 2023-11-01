from game.game_models import BagTiles

class Player:
    def __init__(self, id=0, nickname="nombre/apodo"):
        self.bag_tiles = BagTiles()  # Crear una instancia de BagTiles
        self.score = 0
        self.rack = self.bag_tiles.take(7)  # Llamar al método take con el argumento count
        self.id = id
        self.nickname = nickname
        
    def set_nickname(self):
        self.nickname = input('Ingrese su nombre/apodo: ')
        
    def display_rack(self):
        rack_strings = [str(tile) for tile in self.rack]  # Convierte objetos Tile a cadenas
        print("Sus fichas son: " + ", ".join(rack_strings))

    def is_letter_in_rack(self, word):
        player_letters = {}
        for tile in self.rack:
            letter = tile.letter
            player_letters[letter] = player_letters.get(letter, 0) + 1

        try:
            for letter in word:
                if player_letters[letter] > 0:
                    player_letters[letter] -= 1
                else:
                    raise KeyError(f"Falta la letra '{letter}' para formar la palabra '{word}'.")
        except KeyError as e:
            raise KeyError(e)
        
        return True


    def add_letters(self, letters):
        self.rack.extend(letters)

    def get_score(self):
        return self.score
    
    def update_score(self, points):
        self.get_score
        self.score += points

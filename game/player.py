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


    def add_letters(self, letters):
        self.rack.extend(letters)

    def get_letters(self):
        return self.rack

    def get_score(self):
        return self.score

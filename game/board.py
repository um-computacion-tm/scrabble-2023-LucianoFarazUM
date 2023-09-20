from game.cell import Cell

class Board:
    SIZE = 15

    def __init__(self):
        self.grid = [[Cell() for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def validate_word_inside_board(self, word, location, orientation):
        x, y = location
        len_word = len(word)
        max_x, max_y = self.SIZE, self.SIZE

        if orientation == "H":
            if x < 0 or x + len_word > max_x or y < 0 or y >= max_y:
                return False
        else:
            if x < 0 or x >= max_x or y < 0 or y + len_word > max_y:
                return False

        for i in range(len_word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            if cell.letter and cell.letter != word[i]:
                return False

        return True

    def place_word_on_board(self, word, location, orientation):
        x, y = location
        for i, letter in enumerate(word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            cell.letter = letter

    def validate_word_place_board(self, word, location, orientation):
        if not self.validate_word_inside_board(word, location, orientation):
            return False

        x, y = location
        for i, letter in enumerate(word):
            cell = self.grid[x + i][y] if orientation == "H" else self.grid[x][y + i]
            if cell.letter == letter:
                return False

        return True

    @property
    def is_empty(self):
        return all(not cell.letter for row in self.grid for cell in row)

    def clear_board(self):
        self.grid = [[Cell() for _ in range(self.SIZE)] for _ in range(self.SIZE)]

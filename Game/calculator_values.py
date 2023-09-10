
class CalculateValue:
    @staticmethod
    def calculate(word):
        total_value = 0
        for cell in word:
            if cell.letter is not None:
                total_value += cell.letter.value
        return total_value


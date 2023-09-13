
class CalculateValue:
    @staticmethod
    def calculate(word):
        total_value = 0
        for cell in word:
            if cell.letter is not None:
                total_value += cell.letter.value
        return total_value

    @staticmethod
    def calculate_Word_Value(word):
            total_value = 0
            for cell in word:
                if cell.letter is not None:
                    letter_value = cell.letter.value
                    total_value += letter_value * cell.multiplier  # Multiplicamos el valor de la letra por el multiplicador
            return total_value
    
    
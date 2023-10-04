
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
                if cell.active:  # si está activo, se incluye el multiplicador
                    total_value += letter_value * cell.multiplier
                else:  # si no está activo, solo se añade el valor de la letra
                    total_value += letter_value
        return total_value
from pyrae import dle

class DictionaryConnectionError(Exception):
    pass
 
class Dictionary:
    dle.set_log_level(log_level='CRITICAL')

    def validate_dict(self, word):
        try:
            search_result = dle.search_by_word(word=word)
            if search_result is None or search_result.meta_description == 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.':
                raise DictionaryConnectionError("La palabra no se encuentra en el diccionario.")
            return True
        except Exception as e:
            raise DictionaryConnectionError(f"Error al conectar con el diccionario: {e}")
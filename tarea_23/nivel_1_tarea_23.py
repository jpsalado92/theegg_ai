"""
# Solución de tarea_23
# Autor: Juan Pablo Salado
# Realizado: 2021-05-15

# Tarea: Desarrollar dos funciones que codifiquen y decodifiquen un mensaje utilizando el algoritmo del solitario
"""
import pprint
import random

# Secuencia de palos de la baraja de poker junto al valor que hay que sumar a las cartas bajo ese palo
PALOS = (('♣', 0), ('♦', 13), ('♥', 26), ('♠', 39))

# Secuencia de cartas de un palo dado, junto a su valor lógico correspondiente
VALORES = tuple((str(val), val) for val in range(1, 11)) + (('J', 11), ('Q', 12), ('K', 13))


def get_value_from_letter(letter: str) -> int:
    """
    Devuelve la posición de una letra mayúscula en el abecedario inglés.
    Ejemplo:
        get_value_from_letter('A') -> 1
        get_value_from_letter('Z') -> 26

    :param letter: Letra en el rango (A-Z)
    :return: Entero en el rango (1-26)
    """
    return ord(letter) - ord('@')


def get_letter_from_value(value: int or str) -> str:
    """
    Devuelve la letra correspondiente a una posición en el abecedario inglés.
    Ejemplo:
        get_letter_from_value(1) -> 'A'
        get_letter_from_value(26) -> 'Z'

    :param value: Entero en el rango (1-26)
    :return: Letra en el rango (A-Z)
    """
    return chr(int(value) + ord('@'))


class PokerDeck():
    def __init__(self, seed):
        # Crear una lista de cartas ordenadas con la lógica: (valor, valor_solitario, palo).
        self.cards = [(val[0], val[1] + val_palo, palo) for palo, val_palo in PALOS for val in VALORES] + [
            ('COMODÍN A', 53, 'X'), ('COMODÍN B', 53, 'x')]
        random.seed(seed)
        self.shuffle()

    def shuffle(self):
        # Baraja el mazo de cartas
        random.shuffle(self.cards)

    def locate_joker(self, joker_name):
        # Encuentra la posición del comodín especificado
        if joker_name == 'A':
            return self.cards.index(('COMODÍN A', 53, 'X'))
        elif joker_name == 'B':
            return self.cards.index(('COMODÍN B', 53, 'x'))

    def mover_debajo(self, pos, repeticiones):
        """
        Simula la acción de mover una carta debajo de otra

        :param pos: Posición de la carta a mover
        :param repeticiones: Número de posiciones que se ha de mover la carta especificada
        :return:
        """
        # Localiza la carta de debajo
        swap_pos = pos + 1

        # Resuelve caso en el que la carta especificada sea la última del mazo,
        # en cuyo caso, la nueva posición sera debajo de la primera carta del mazo
        if swap_pos == len(self.cards):
            swap_pos -= len(self.cards)

        # Se intercambian las cartas de lugar
        self.cards[pos], self.cards[swap_pos] = self.cards[swap_pos], self.cards[pos]

        # Se resta 1 al contador de movimientos
        repeticiones -= 1

        # Si aún quedan movimientos, repetimos la jugada
        if repeticiones:
            self.mover_debajo(swap_pos, repeticiones)

    def get_solitaire_code(self):
        # Intercambio del comodín A con la carta que tiene debajo
        # (si el comodín está al final de la baraja, se pone debajo de la primera carta)
        self.mover_debajo(self.locate_joker('A'), 1)

        # Intercambio del comodín B con la carta que hay debajo de la que tiene debajo
        self.mover_debajo(self.locate_joker('B'), 2)

        # Cortar la baraja en tres conjuntos,
        # intercambiando las cartas antes del primer comodín con las cartas que están detrás del segundo comodín
        pos_a = self.locate_joker('A')
        pos_b = self.locate_joker('B')

        if pos_a > pos_b:
            pos_primero = pos_b
            pos_ultimo = pos_a
        else:
            pos_primero = pos_a
            pos_ultimo = pos_b

        self.cards = \
            self.cards[pos_ultimo + 1:len(self.cards)] \
            + self.cards[pos_primero:pos_ultimo + 1] \
            + self.cards[0:pos_primero]

        # Partir el mazo en 3 conjuntos:
        # Conj. 1: Tantas cartas como indique el valor de la última carta. Si el valor es 53 (comodín), no se hace nada
        # Conj. 2: Cartas sobrantes tras el primer corte, salvo la última carta
        # Conj. 3: Última carta
        last_card_val = self.cards[-1][1]

        if last_card_val != 53:
            self.cards = \
                self.cards[last_card_val:-1] \
                + self.cards[0:last_card_val] \
                + self.cards[-1:len(self.cards)]

        # El valor buscado será el de aquella carta cuya posición en el mazo coincida con el valor de la primera carta
        first_card_val = self.cards[0][1]
        output_card_val = self.cards[first_card_val][1]

        # Devolvemos el valor en un generador
        yield output_card_val

    def __str__(self):
        return pprint.pformat(self.cards)


def codificador(text: str, deck: object) -> str:
    """
    Codifica un texto con el algoritmo del solitario

    :param text: Texto a codificar
    :param deck: Mazo inicializado, que comparten emisor y receptor.
    :return: Texto codificado
    """

    # Eliminar espacios y poner texto en mayúsculas
    text = text.replace(' ', '').upper()

    # Hacer grupos de 5 caracteres y rellenar con "X" el grupo que no llegue a 5
    code = [text[i:i + 5].ljust(5, 'X') for i in range(0, len(text), 5)]

    # Obtener valor de cada letra y le suma un valor generado con el algoritmo del solitario
    code = [[get_value_from_letter(letter) + next(deck.get_solitaire_code()) for letter in group] for group in code]

    # Limpiar valores mayores que 26
    code = [[(num if (num <= 26) else num - 26) for num in group] for group in code]
    code = [[(num if (num <= 26) else num - 26) for num in group] for group in code]

    # Pasar mezcla a letras codificadas
    code = [''.join([get_letter_from_value(value) for value in group]) for group in code]

    return code


def decodificador(code: list, deck: object) -> str:
    """
    Decodifica un texto con el algoritmo del solitario

    :param code: Código cifrado por el emisor.
    :param deck: Mazo inicializado, que comparten emisor y receptor.
    :return:
    """
    # Obtener valor de cada letra y le resta un valor generado con el algoritmo del solitario
    code = [[get_value_from_letter(letter) - next(deck.get_solitaire_code()) for letter in group] for group in code]
    code = [[(num if (num > 0) else num + 26) for num in group] for group in code]
    code = [[(num if (num > 0) else num + 26) for num in group] for group in code]

    # Pasar mezcla a letras
    code = [''.join([get_letter_from_value(value) for value in group]) for group in code]

    return code


if __name__ == "__main__":
    mazo_emisor = PokerDeck(seed=1)
    mazo_receptor = PokerDeck(seed=1)

    text = "Vaya tareita"
    coded_text = codificador(text, mazo_emisor)
    decoded_text = decodificador(coded_text, mazo_receptor)
    print(decoded_text)

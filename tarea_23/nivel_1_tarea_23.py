"""
# Solución de tarea_23
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-15
# Fecha última revisión: 2021-06-02

# Tarea: Desarrollar funciones que codifiquen y decodifiquen un mensaje utilizando el algoritmo del solitario.
"""
import pprint
import random
import re
import unicodedata


def normalize_text(text):
    """Normaliza el texto a encriptar, garantizando la aplicabilidad del algoritmo del solitario"""

    # Pasar texto a mayúsculas
    text = text.upper()

    # Reemplazar caracteres especiales (tildes, ñ)
    text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))

    # Extraer signos de puntuación, retornos de línea, espacios, números y símbolos
    text = re.sub(r'[,.!?\-\/@\\(\\\\)\\123456789\n\s"]', '', text)

    if re.match('[^A-Z]', text):
        raise ValueError("Se han introducido caracteres no soportados, revisa el texto a encriptar")
    return text


def format_text(text):
    """Divide un texto en grupos de 5 caracteres y rellena con "X" el grupo que no llegue a 5"""
    return [text[i:i + 5].ljust(5, 'X') for i in range(0, len(text), 5)]


def get_value_from_letter(letter: str) -> int:
    """
    Devuelve la posición de una letra mayúscula en el abecedario inglés.
    :param letter: Letra en el rango (A-Z)
    :return: Entero en el rango (1-26)
    """
    return ord(letter) - ord('@')


def get_letter_from_value(value: int or str) -> str:
    """
    Devuelve la letra correspondiente a una posición en el abecedario inglés.
    :param value: Entero en el rango (1-26)
    :return: Letra en el rango (A-Z)
    """
    return chr(int(value) + ord('@'))


class PokerDeck:
    # Secuencia de palos de la baraja de poker junto al valor que hay que sumar a las cartas bajo ese palo
    palos = (('♣', 0), ('♦', 13), ('♥', 26), ('♠', 39))
    # Secuencia de cartas de un palo dado, junto a su valor lógico correspondiente
    valores = tuple((str(val), val) for val in range(1, 11)) + (('J', 11), ('Q', 12), ('K', 13))

    def __init__(self, seed):
        """Inicializa un mazo de cartas ordenadas con la lógica: (valor, valor_solitario, palo)"""
        # Añadir cartas normales
        self.cards = [(val[0], val[1] + val_palo, palo) for palo, val_palo in self.palos for val in self.valores]
        # Añadir comodines
        self.cards += [('COMODÍN A', 53, 'X'), ('COMODÍN B', 53, 'x')]
        # Establecer semilla para generación de ordenaciones semialeatorias
        random.seed(seed)
        # Barajar mazo
        self.shuffle()

    def shuffle(self):
        """Baraja el mazo de cartas"""
        random.shuffle(self.cards)

    def locate_joker(self, joker_name):
        """Encuentra la posición del comodín especificado"""
        if joker_name == 'A':
            return self.cards.index(('COMODÍN A', 53, 'X'))
        elif joker_name == 'B':
            return self.cards.index(('COMODÍN B', 53, 'x'))

    def move_down(self, pos, rep: int):
        """
        Simula la acción de colocar una carta debajo de otra

        :param pos: Posición de la carta a mover
        :param rep: Número de operaciones consecutivas
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
        rep -= 1

        # Si aún quedan movimientos, repetimos la jugada
        if rep:
            self.move_down(swap_pos, rep)

    def get_solitaire_code(self):
        # Intercambio del comodín A con la carta que tiene debajo
        # (si el comodín está al final de la baraja, se pone debajo de la primera carta)
        self.move_down(self.locate_joker('A'), 1)

        # Intercambio del comodín B con la carta que hay debajo de la que tiene debajo
        self.move_down(self.locate_joker('B'), 2)

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


def codificador(text: str, deck: object) -> list:
    """
    Codifica un texto con el algoritmo del solitario

    :param text: Texto a codificar
    :param deck: Mazo inicializado, que comparten emisor y receptor.
    :return: Texto codificado
    """
    code = normalize_text(text)
    code = format_text(code)

    # Obtener valor de cada letra y sumar un valor generado con el algoritmo del solitario
    code = [[get_value_from_letter(letter) + next(deck.get_solitaire_code()) for letter in group] for group in code]

    # Limpiar valores mayores que 26 (dos ocasiones como máximo)
    code = [[(num - 26 if num > 26 else num) for num in group] for group in code]
    code = [[(num - 26 if num > 26 else num) for num in group] for group in code]

    # Pasar mezcla a letras codificadas
    code = [''.join([get_letter_from_value(value) for value in group]) for group in code]

    return code


def decodificador(code: list, deck: object) -> list:
    """
    Decodifica un texto con el algoritmo del solitario

    :param code: Código cifrado por el emisor.
    :param deck: Mazo inicializado, que comparten emisor y receptor.
    :return:
    """
    # Obtener valor de cada letra y le resta un valor generado con el algoritmo del solitario
    code = [[get_value_from_letter(letter) - next(deck.get_solitaire_code()) for letter in group] for group in code]

    # Limpiar valores negativos (dos ocasiones como máximo)
    code = [[(num if (num > 0) else num + 26) for num in group] for group in code]
    code = [[(num if (num > 0) else num + 26) for num in group] for group in code]

    # Pasar mezcla a letras
    code = [''.join([get_letter_from_value(value) for value in group]) for group in code]

    return code


def solitario(text, mazo_emisor, mazo_receptor):
    coded_text = codificador(text, mazo_emisor)
    decoded_text = decodificador(coded_text, mazo_receptor)
    return coded_text, decoded_text


if __name__ == "__main__":
    # Crear mazos idénticos
    mazo_emisor = PokerDeck(seed=1)
    mazo_receptor = PokerDeck(seed=1)
    mensaje = input("Introduce el texto a encriptar: ")
    coded_text, decoded_text = solitario(mensaje, mazo_emisor, mazo_receptor)
    print(f"Texto codificado: {coded_text}")
    print(f"Texto decodificado: {decoded_text}")
    # print(f"Estado del mazo:")
    # print(mazo_emisor)

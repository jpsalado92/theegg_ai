"""
# Solución de tarea_38_2
# Autor: Juan Pablo Salado
# Fecha creación: 2021-06-21

# Tarea:
Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso.
Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras.
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la
frase invertida.
"""


def reverse_words(phrase: str) -> str:
    """
    Dada una cadena de texto con palabras separadas por espacios, da la vuelta al orden de las palaras
    :param phrase: Cadena de texto
    :return: Cadena de texto invertida
    """
    return ' '.join(reversed(phrase.split(' ')))

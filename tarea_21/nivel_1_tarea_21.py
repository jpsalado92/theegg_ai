"""
# Solución de tarea_21
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-08
# Fecha última revisión: 2021-07-02

# Referencias:
Calcular número de decimales de un número: https://github.com/AlejandroGarcia987/theegg_ai

# Tarea: Desarrollar un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales),
obtenga y muestre la correspondiente fracción irreducible. Por ejemplo, el número 0,25 se puede obtener a partir de
25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un
denominador que son primos entre sí.
"""
from fractions import Fraction


def validate_input(value, verbose=False) -> bool:
    """Valida el input para el programa asociado"""
    # Comprobar si el número es convertible a float
    try:
        float_value = float(value)
    except ValueError:
        if verbose:
            print("Mete algo parecido a un número por favor")
        return False

    # Comprobar si el número está en el rango indicado
    if float_value < 0.0001 or float_value > 0.9999:
        if verbose:
            print("Tío, ¡¡que escribas un valor en el rango 0,0001-0,9999!!")
        return False

    # Comprobar si el número tiene menos del número máximo de decimales
    if str(float_value)[::-1].find('.') > 4:
        if verbose:
            print("¡Intenta un número con un máximo de 4 decimales!")
        return False

    # Manejando un número válido
    return True


def get_fraction(value):
    """Devuelve el numerador y denominador del número decimal introducido"""
    return str(Fraction(float(value)).limit_denominator())


if __name__ == "__main__":
    while True:
        input_value = input("Escribe un valor entre 0,0001 y 0,9999 con un máximo de 4 decimales: ")
        if validate_input(input_value, verbose=True):
            break

    print("La fracción que buscas es: " + get_fraction(input_value))

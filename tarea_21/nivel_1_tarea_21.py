# Solución de tarea_21
# Autor: Juan Pablo Salado
# Realizado: 2021-05-08

from fractions import Fraction


def correct_input_check(input):
    # Comprobar si el número es convertible a float
    try:
        fval = float(input)
    except ValueError:
        print("Mete algo parecido a un número por favor")
        return False

    # Comprobar si el número está en el rango indicado
    if fval < 0.0001 or fval > 0.9999:
        print("Tío, ¡¡que escribas un valor en el rango 0,0001-0,9999!!\nTu número: ")
        return False

    # Comprobar si el número tiene menos del número máximo de decimales
    if len(input) > 6:
        print("¡Intenta un número con un máximo de 4 decimales!")
        return False

    # Manejando un número válido
    return True


if __name__ == "__main__":
    val = input("Escribe un valor entre 0,0001 y 0,9999 con un máximo de 4 decimales:\nTu numero: ")

    while not correct_input_check(val):
        val = input()

    print("La fracción que buscas es: " + str(Fraction(float(val)).limit_denominator()))

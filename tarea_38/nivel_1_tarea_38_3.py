"""
# Solución de tarea_38_3
# Autor: Juan Pablo Salado
# Fecha creación: 2021-06-21

# Tarea:
Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras.
Por ejemplo, 79197 y 324423 son palíndromos.

En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. Usted debe encontrar el menor entero M tal que M >= N
que es primo y M es un palíndromo N.
Por ejemplo, si N es 31, entonces la respuesta es 101.

Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.
Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
"""


def is_prime(number) -> bool:
    """Checks whether a number is a prime number or not"""
    aux_var = 2
    while number % aux_var != 0:
        aux_var += 1
        if aux_var == number - 1:
            return True
    return False


def is_palindrome(number) -> bool:
    """Checks whether a number is a palindrome or not"""
    return True if int(str(number)[::-1]) == number else False


def get_closest_higher_or_equal_prime_palindrome_number(number) -> int:
    """Gets the closest equal or higher number which is, at the same time, a prime and palindrome number"""
    while not (is_palindrome(number) and is_prime(number)):
        number += 1
    return number

"""
# Solución de tarea_45
# Autor: Juan Pablo Salado
# Fecha creación: 2021-06-23

# Tarea:
Tenemos la siguiente lista de elementos: [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].
1.- Construye tu propio algoritmo para ordenarlo de menor a mayor.
2.- Busca el número 874 utilizando el algoritmo secuencial y el binario. En cada iteración se debe sumar +1
de modo que al final del programa se debe indicar el número de iteraciones realizadas por cada
algoritmo hasta encontrar el elemento.
3.- Realiza el análisis en Notación Big O (visto en la tarea #44) y describe tu conclusiones en un
documento de texto.

Debes subir a tu repositorio GitHub tanto el programa (en el lenguaje de programación que hayas
elegido) y el documento de texto explicativo y razonado sobre el rendimiento y los tiempos de ejecución
de cada algoritmo en notación O Grande. Por supuesto, no te olvides del diccionario.
"""


def sequential_search(iterable, search_value):
    """
    Implementación del algoritmo de búsqueda secuencial.
    Devuelve 0 si el elemento no se ha encontrado.
    Si el elemento se ha encontrado se devuelve el número de iteraciones hasta llegar a él.
    """
    # Iniciar búsqueda y contador
    i = 0
    while i < len(iterable):

        # Aumentar contador de iteración
        i += 1

        if iterable[i] == search_value:
            # Elemento encontrado
            return i

    # Elemento no encontrado
    return 0


def binary_search(iterable, search_value):
    """
    Implementación del algoritmo de búsqueda binaria.
    Devuelve 0 si el elemento no se ha encontrado.
    Si el elemento se ha encontrado se devuelve el número de iteraciones hasta llegar a él.
    """
    # Ordenar lista (necesario para que el algoritmo funcione)
    iterable = sorted(iterable)

    # Descartar búsqueda si el número no está en el rango del iterable
    if search_value > iterable[-1] or search_value < iterable[0]:
        return 0

    # Iniciar búsqueda y contador
    i = 0
    while True:

        # Aumentar contador de iteración
        i += 1

        # Cubrir caso en el que el iterable sólo tiene un elemento
        if len(iterable) == 1:
            if iterable[0] == search_value:
                return i
            else:
                return 0

        middle_pos = int(len(iterable) / 2)
        middle_val = iterable[middle_pos]

        # Caso en el que el valor está en el punto medio del iterable
        if middle_val == search_value:
            return i

        # Caso en el que el valor está en la franja izquierda del iterable
        if search_value < middle_val:
            iterable = iterable[0:middle_pos]

        # Caso en el que el valor está en la franja derecha del iterable
        elif search_value > middle_val:
            iterable = iterable[(middle_pos + 1):]

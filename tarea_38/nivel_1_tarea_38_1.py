"""
# Solución de tarea_38_1
# Autor: Juan Pablo Salado
# Fecha creación: 2021-06-20

# Tarea:
Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN,
y el objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.
Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C),
guanina (G) y timina (T).

En el ejemplo de las secuencias "ATGTCTTCCTCGA" y "TGCTTCCTATGAC" el resultado es "CTTCCT", porque que es el conjunto
ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida.
"""


def get_major_common_substring(seq_1: str, seq_2: str) -> str:
    """
    Función que calcula la mayor subsecuencia común entre dos strings.
    El cálculo se basa en la programación dinámica, que trata de mantener un tiempo de ejecución lineal a medida que
    crezcan los parámetros de entrada. Para ello, se construye una tabla de tal manera que:
        1. Los valores de las celdas indican el parámetro a optimizar. En este caso el mayor número de elementos en común
        2. Cada celda es un subproblema, una parte reducida del problema a resolver. En este caso son substrings.
        3. Los valores se rellenan de fila en fila, de izquierda a derecha.

    La fórmula para llegar a la solución consiste en encontrar la celda de mayor valor, rellenando las celdas de la
    siguiente manera:
        · Si las letras de las celdas no coinciden el valor es 0
        · Si las letras de las celdas coinciden, el valor es 1. En caso de que haya una celda vecina en la fila superior
         en la columna directamente a la izquierda, se le suma el valor de esa celda.



    Ejemplo: Para las secuencias HOLA y OLA la matriz sin rellenar sería:

          H O L A
        O . . . .
        L . . . .
        A . . . .

    Los valores a rellenar y matrices de los subproblema correspondientes serían:

    · Celda [0, 0]: En este caso las letras no coinciden, por lo tanto valor 0

          H
        O 0

    · Celda [0, 1]: En este caso las letras sí coinciden, por lo tanto valor 1

          H O
        O 0 1

    · Celda [1, 2]: En este caso las letras sí coinciden, por lo tanto valor 1, más el valor de la celda vecina.

          H O L A
        O 0 1 0 0
        L 0 0 2 .

    · Así, la matriz final quedaría como:

          H O L A
        O 0 1 0 0
        L 0 0 2 0
        A 0 0 0 3

    · Por último podemos sacar la secuencia partiendo del valor máximo de la tabla (VAL:3) y su número de fila (NF:2).
        msc = "OLA"[(NF-VAL+1):(NF+1)]
        msc = "OLA"[(2-3+1):(2+1)]
        msc = "OLA"[0:3]


    :param seq_1: Secuencia en formato string 1
    :param seq_2: Secuencia en formato string 2
    :return: Mayor subcadena común
    """
    table = []
    max_row_idx = max_val = 0

    # Se construye una matriz para resolver el problema por programación dinámica
    for row_idx in range(len(seq_1)):
        row = []

        for col_idx in range(len(seq_2)):

            # Coincide la letra de la fila y columna
            if seq_1[row_idx] == seq_2[col_idx]:

                # Caso especial, nos encontramos en la primera fila o columna
                if not col_idx or not row_idx:
                    val = 1
                # Caso normal, 1 + valor vecino
                else:
                    val = 1 + table[row_idx - 1][col_idx - 1]

            # No coincide la letra de la fila y columna, valor 0
            else:
                val = 0

            # Registro valor y posición de la celda con valor máximo
            if val > max_val:
                max_val = val
                max_row_idx = row_idx

            row.append(val)
        table.append(row)
    return seq_1[(max_row_idx - max_val + 1):(max_row_idx + 1)]

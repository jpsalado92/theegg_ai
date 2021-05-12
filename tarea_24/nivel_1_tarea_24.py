"""
# Solución de tarea_24
# Autor: Juan Pablo Salado
# Realizado: 2021-05-12

# Tarea: Desarrollar un programa donde una vez enviado un valor decimal a una función este lo convierta a binario
 y nos lo devuelva.
"""


def convertidor_digital(acu: int) -> str:
    """
    Función que convierte valores decimales en binario.
    :param acu: Número decimal a convertir.
    :return: Número binario en formato string
    """
    # Manejar valor 0
    if acu == 0:
        return '0'

    # Inicializar cadena de texto vacía
    num_bin = ''

    # Bucle de ejecución
    while acu != 1:
        num_bin = ''.join((str(acu % 2), num_bin))
        acu = acu // 2

    return ''.join(('1', num_bin))


if __name__ == "__main__":
    print(convertidor_digital(4815162342))

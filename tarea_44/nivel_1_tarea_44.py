import time


def suma_lineal(n: int) -> tuple:
    """
    Suma uno a uno
    :param n: Cantidad de números enteros a partir del 0 a sumar
    :return: Suma y tiempo de ejecución
    """
    t0 = time.time()
    suma = 0
    for i in range(n + 1):
        suma += i
    t1 = time.time()
    return int(suma), "{:.2e}".format(t1 - t0)


def suma_constante(n: int) -> tuple:
    """
    Suma según el algoritmo de Gauss
    :param n: Cantidad de números enteros a partir del 0 a sumar
    :return: Suma y tiempo de ejecución

    Nota: El tiempo es demasiado pequeño, por lo que t1 - t0 puede dar 0 en varios sistemas.
    """
    t0 = time.time()
    suma = (n / 2) * (n + 1)
    t1 = time.time()
    return int(suma), "{:.2e}".format(t1 - t0)


if __name__ == "__main__":
    n = 10

    for i in range(11):
        print(f"Números a sumar, desde el 0 al {n}")
        print("Método suma convencional:" + str(suma_lineal(n)))
        print("Método suma de Gauss:" + str(suma_constante(n)))
        print()
        n *= 10

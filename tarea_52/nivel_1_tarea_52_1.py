"""
# Solución de tarea_52_1
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-28
# Fecha revisión: 2021-06-08

# Tarea: Desarrolla un programa que sirva para:
- Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el
  número 0, el cual no debe guardarse.
- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su
  primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
- Recorrer la lista para imprimir la sumatoria de todos los elementos.
- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores
  que el número dado. Imprimir esta nueva lista, iterando por ella.
- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una
  compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si
  la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
"""

import collections


def get_inputs():
    """ Interfaz para solicitar números al usuario y guardarlos en una lista """
    input_list = []
    print("Aupa muchacho, vamos a llenar una lista de números!")
    while True:
        input_val = input("Inserta un número para la lista, si es 0 terminamos esta fase")
        if input_val != '0':
            try:
                f_val = float(input_val)
                input_list.append(f_val)
            except ValueError:
                print("Mete algo parecido a un número por favor")
                continue
        else:
            print(f"Lista de números añadidos: {input_list}")
            return input_list


def get_val_and_remove_if_exist(input_list, input_val=None):
    """
    Comprueba si un número `input_val` está en la lista `input_list`, en caso afirmativo, lo elimina.
    NOTA: No es necesario retornar la lista, ya que se trabaja sobre sí misma
    """
    if not input_val:
        while True:
            input_val = input(
                "Inserta un número, se comprobará si está en la lista, si es así, se eliminará la primera ocurrencia")
            try:
                input_val = float(input_val)
                break
            except ValueError:
                print("Mete algo parecido a un número por favor")
                continue

    if input_val in input_list:
        input_list.remove(input_val)
        print(f"Lista de números: {input_list}")
    else:
        print("El valor insertado no se encuentra entre los valores disponibles")


def sum_list_elements(input_list):
    """ Suma los elementos de la lista """
    print(f"Sumatorio de los elementos dela lista: {sum(input_list)}")


def filter_list(input_list, th_val=None):
    """ Filtra una lista según un valor umbral y la devuelve """
    if not th_val:
        print("Inserta el umbral a partir de cual se filtraran los valores de la lista anterior")
        while True:
            input_val = input()
            try:
                th_val = float(input_val)
                break
            except ValueError:
                print("Mete algo parecido a un número por favor")
                continue

    filtered_list = [x for x in input_list if x < th_val]
    print(f"Lista filtrada: {filtered_list}")
    return filtered_list


def get_frequency_list(input_list):
    """ Devuelve e imprime un diccionario de frecuencias de términos de una lista """
    freq_dict = collections.Counter(input_list)
    freq_list = [(v, f) for v, f in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)]
    print(f"Lista de frecuencias: {freq_list}")
    return freq_list


if __name__ == "__main__":
    inputs = get_inputs()
    get_val_and_remove_if_exist(inputs)
    sum_list_elements(inputs)
    inputs_filtrados = filter_list(inputs)
    lista_frecuencias = get_frequency_list(inputs)

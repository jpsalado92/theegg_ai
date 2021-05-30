"""
# Solución de tarea_52
# Autor: Juan Pablo Salado
# Realizado: 2021-05-28
"""

import collections


def subtask1():
    """
    1.- Desarrolla un programa que sirva para:
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
    input_list = []
    while True:
        input_val = input("Inserta un número")
        if input_val != '0':
            try:
                f_val = float(input_val)
                input_list.append(f_val)
            except ValueError:
                print("Mete algo parecido a un número por favor")
                continue
        else:
            break

    print(f"Lista de números añadidos: {input_list}")

    input_val = input("Inserta un número, si el número está en la lista, se borrará la primera ocurrencia")
    if float(input_val) in input_list:
        input_list.remove(float(input_val))
        print(f"Lista de números: {input_list}")
    else:
        print("El valor insertado no se encuentra entre los valores disponibles")

    print(f"Sumatorio de los elementos dela lista: {sum(input_list)}")

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
    print(f"Lista filtrada:1 {filtered_list}")

    freq_dict = collections.Counter(filtered_list)
    freq_list = [(v, f) for v, f in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)]
    print(f"Lista de frecuencias: {freq_list}")


def subtask2():
    """
    2.- Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela,
    finalizando al ingresar ?x?. A continuación, solicitar que ingrese los nombres de los alumnos de nivel
    secundario, finalizando al ingresar ?x?.
    - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
    - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    """

    def get_names(msg):
        name_list = []
        while True:
            print(msg)
            input_val = input()
            if input_val != "?x?":
                name_list.append(input_val)
                continue
            else:
                break
        return name_list

    alumnos_primaria = get_names("Inserta los nombres de pila de primaria")
    alumnos_secundaria = get_names("Inserta los nombres de pila de secundaria")
    alumnos_primaria_set = set(alumnos_primaria)
    alumnos_secundaria_set = set(alumnos_secundaria)
    print(f"Alumnos en primaria: {alumnos_primaria}")
    print(f"Alumnos en primaria, sin repeticiones: {alumnos_primaria_set}")
    print(f"Alumnos en secundaria: {alumnos_secundaria}")
    print(f"Alumnos en primaria, sin repeticiones: {alumnos_secundaria_set}")
    print(f"Alumnos en ambos cursos, sin repeticiones: {alumnos_primaria_set.union(alumnos_secundaria_set)}")


if __name__ == "__main__":
    subtask1()
    subtask2()

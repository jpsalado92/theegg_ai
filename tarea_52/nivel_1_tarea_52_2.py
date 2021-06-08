"""
# Solución de tarea_52_2
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-28
# Fecha revisión: 2021-06-08
# Tarea:
Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela,
finalizando al ingresar ?x?. A continuación, solicitar que ingrese los nombres de los alumnos de nivel
secundario, finalizando al ingresar ?x?.
    - Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
    - Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    - Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""


def get_names(msg):
    """ Recoge una lista de nombres hasta que se ingrese la cadena `?x?` """
    name_list = []
    while True:
        print(msg)
        input_val = input()
        if input_val != "?x?":
            name_list.append(input_val)
            continue
        else:
            return name_list


if __name__ == "__main__":
    # Recoger nombres de los dos cursos
    alumnos_primaria = get_names("Inserta los nombres de pila de primaria")
    alumnos_secundaria = get_names("Inserta los nombres de pila de secundaria")

    # Forma un `set`, donde no se repiten elementos entre sí, de las listas anteriormente recogidas
    set_alumnos_primaria = set(alumnos_primaria)
    set_alumnos_secundaria = set(alumnos_secundaria)

    # Tarea 1: Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
    print(f"Nombres en primaria, sin repeticiones: {set_alumnos_primaria}")
    print(f"Nombres en secundaria, sin repeticiones: {set_alumnos_secundaria}")
    print(f"Nombres en ambos cursos, sin repeticiones: {set_alumnos_primaria.union(set_alumnos_secundaria)}")

    # Tarea 2: Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    print(f"Nombres repetidos en ambos cursos: {set_alumnos_primaria.intersection(set_alumnos_secundaria)}")

    # Tarea 3: Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
    print(f"Nombres en primaria no repetidos en secundaria: {set_alumnos_primaria.difference(set_alumnos_secundaria)}")

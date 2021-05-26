"""
# Solución de tarea_41
# Autor: Juan Pablo Salado
# Realizado: 2021-05-26

# Tarea: Mediante técnicas de regex calcular el número de caracteres, el número de palabras y ranking de palabras por
frecuencia de uso del siguiente texto (la aplicación debe servir para cualquier otro texto)
"""

import collections
import re


def main():
    # Carga de texto
    with open("nivel_1_tarea_41.txt", 'r', encoding='utf8') as f:
        text = f.read()

    # Quitar caracteres de retorno de línea
    text = re.sub(r'\n', ' ', text)

    # Quitar signos de puntuación
    text = re.sub(r'[,.!?\\-\\"]', '', text)

    # Contar número de caracteres
    print(f"Número de caracteres sin retornos de línea ni signos de puntuación: {len(text)}", end='\n\n')

    # Pasar texto a minúsculas
    text = text.lower()

    # Obtener listado de palabras
    lista_palabras = text.split()

    print(f"Número de palabras: {len(lista_palabras)}", end='\n\n')

    # Obtener diccionario de frecuencias ordenado
    frequency = collections.Counter(lista_palabras)
    frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

    print(f"Número de palabras distintas: {len(frequency)}", end='\n\n')
    print("Diccionario de frecuencias:")
    print(frequency)


if __name__ == "__main__":
    main()

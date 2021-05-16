"""
# Solución de tarea_24
# Autor: Juan Pablo Salado
# Realizado: 2021-05-16

# Tarea: Teniendo en cuenta el límite de capacidad de un camión [kg], y una población de vacas N, obtener la mejor
selección de ganado teniendo en cuenta su producción y peso.

# Notas: Uno de los primeros enfoques que le dí al problema, consistía en obtener la eficiencia (ϵ) de las vacas, ordenar
las vacas según ella, y cargar vacas hasta completar el camión en ese orden. Intuitivamente parece ser correcto, pero no
es una solución perfecta, ya que el algoritmo no funcionaría en el siguiente caso:

    Ejemplo (enfoque eficiencias):
    ------------------------------
    Para un límite de peso "cap_lim = 1300":

    {'id_vaca': 0, 'gramos_vaca[kg]': 1000, 'prod_vaca[L]': 500} ->  ϵ = 0.5 [L/kg]
    {'id_vaca': 1, 'gramos_vaca[kg]': 650, 'prod_vaca[L]': 300} ->  ϵ = 0.46 [L/kg]
    {'id_vaca': 2, 'gramos_vaca[kg]': 650, 'prod_vaca[L]': 300} ->  ϵ = 0.46 [L/kg]

    En este caso entraría únicamente la vaca '0', por lo que el camión se habría llenado y solo podríamos producir 500 L
    de leche. Sin embargo, la mejor combinación sería cargar la vaca '1' y '2', ya que a lo sumo, darían 600L de leche.

  Dada la naturaleza del problema, si buscamos una solución perfecta, parece lógico que pensar que habría que probar
todas las posibilidades de carga, sin embargo, podemos caer en la tentación de programar un algoritmo cuyo tiempo de
procesamiento crezca exponencialmente con el número de vacas (n!). Sin embargo, mediante la programación dinámica, es
posible hacer que el tiempo de procesamiento crezca linealmente (con el ahorro de tiempo que ello supone) con el número
de vacas. La clave consiste en ir construyendo una tabla que vaya construyendo la solución progresivamente.

"""
import random

# Parámetros habituales de las vacas según `San Google`
RANGO_PESO_VACA = (640, 900)
RANGO_PROD_LECHE = (18, 24)

# Cantidad de vacas en la pradera
NUM_VACAS = 500

# Peso de carga límite [kg]
CAP_MAX_KG = 20000


def normal_obs(dmin: int, dmax: int) -> float:
    """
    Función que en base a valores de un rango, devuelve observaciones que siguen una distribución normal.
    :param dmin: Valor (µ - 3σ), valor cercano al mínimo de la distribución normal
    :param dmax: Valor (µ + 3σ), valor cercano al máximo de la distribución normal
    :return:
    """
    mu = (dmax - dmin) / 2 + dmin
    sigma = (dmax - dmin) / 6
    return int((random.gauss(mu, sigma)))


def find_best_set(item_list, max_cap):
    """
    Algoritmo que en base a una lista de unidades (tuplas) y un parámetro limitante,
    devuelve un subconjunto de unidades que maximiza un valor consolidado sin rebasar el parámetro limitante.

    Caso de uso:
    -----------
    Dado un camión con una carga limitada y un conjunto de vacas, seleccionar un subconjunto de vacas que den más leche
    sin rebasar la capacidad mencionada.

    :param item_list[list]: Lista de tuplas.
      Cada tupla tiene el formato:
        (identificador[string], valor_limitante[int],  valor_a_maximizar[int])
      Siguiendo el ejemplo del caso de uso:
        (identificador_de_vaca, peso_de_vaca, produccion_de_vaca)
    :param max_cap[int]: Valor limitante. (Peso del camión)
    :return[tuple]: (valor_maximo_consolidado[int], peso_total_subconjunto[int], lista_de_identificadores[tuple])
    """
    table = []
    for i in range(len(item_list)):
        row = []

        for j in range(max_cap):
            current_id, current_weight, current_val = item_list[i]
            # Caso singular: Rellenar valores de la primera fila
            if i == 0:
                remaining_weight = j + 1 - current_weight
                if remaining_weight < 0:
                    cell_val = (0, 0, ())
                else:
                    cell_val = (current_val, current_weight, (current_id,))
            else:
                previous_val, previous_weight, previous_ids = table[i - 1][j]

                remaining_weight = j + 1 - current_weight

                if remaining_weight < 0:
                    cell_val = (previous_val, previous_weight, previous_ids)

                elif remaining_weight == 0:
                    if current_val >= previous_val:
                        cell_val = (current_val, current_weight, (current_id,))
                    else:
                        cell_val = (previous_val, previous_weight, previous_ids)

                elif remaining_weight > 0:
                    filling_val, filling_weight, filling_ids = table[i - 1][remaining_weight - 1]
                    if current_val + filling_val >= previous_val:
                        cell_val = (
                            current_val + filling_val, current_weight + filling_weight, filling_ids + (current_id,))
                    else:
                        cell_val = (previous_val, previous_weight, previous_ids)

            row.append(cell_val)
        table.append(row)
    return table[-1][-1]


if __name__ == "__main__":
    # Generar un rebaño de vacas, basándonos en los parámetros establecidos al principio del script
    cows = tuple(
        {'id': i + 1,
         'kg': normal_obs(*RANGO_PESO_VACA),
         'L': normal_obs(*RANGO_PROD_LECHE)}
        for i in range(NUM_VACAS))

    # Convertir el rebaño a un formato procesable por el algoritmo que calculará la mejor selección
    item_list = [(cow['id'], cow['kg'], cow['L']) for cow in cows]

    # Obtener los valores de la mejor selección
    produccion, peso_total, seleccion = find_best_set(item_list=item_list, max_cap=CAP_MAX_KG)
    print("RESULTADOS\n----------")
    print(f"La selección óptima da una producción de:\n  {produccion} [L/día]\n")
    print(f"El peso total de la selección óptima es de:\n  {peso_total} [kg]\n")
    print(f"La selección óptima está compuesta por los identificadores:\n  {seleccion}")

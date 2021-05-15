"""
# Solución de tarea_33
# Autor: Juan Pablo Salado
# Realizado: 2021-05-15

# Tarea: Dibujar y programar un combate Pokémon.
"""


class Pokemon():
    def __init__(self, hp, pa):
        self.hp = hp
        self.pa = pa


def combate():
    # Inicializar pokemons con vida y puntos de ataque
    pikachu = Pokemon(100, 50)
    charmander = Pokemon(100, 45)

    # Dar primer turno a la rata
    pikachu_turn = False

    # Combate hasta que alguien moche
    while not any((hp <= 0 for hp in (pikachu.hp, charmander.hp))):
        if pikachu_turn:
            charmander.hp -= pikachu.pa
            pikachu_turn = False
        else:
            pikachu.hp -= charmander.pa
            pikachu_turn = True

        print("NUEVO TURNO!:")
        print(f"Vida Pikachu: {pikachu.hp}")
        print(f"Vida Charmander: {charmander.hp}")
        print()

    # Alguien mochó
    if pikachu.hp > 0:
        print("Charmander desfalleció...")
        print("Pikachu wins!")
    else:
        print("Pikachu desfalleció...")
        print("Charmander wins!")


if __name__ == "__main__":
    combate()

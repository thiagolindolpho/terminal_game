import random
import time
from calculate_dmg import calculate_damage
#(hero["damage"] - (hero["damage"] - 1))


def combat_start(hero, enemy):

    enemy_total_health = enemy["health"]
    enemy_max_health = enemy["health"]


    while True:
        enemy_total_health - calculate_damage(hero, enemy) # <-- calculo de dano vem aqui

        print(f"enemy total health: {enemy_max_health}")
        print(f"enemy_health: {enemy_max_health} - hero_dmg: {hero["damage"]}")
        print("\n")
        print(f"enemy atual health: {enemy_total_health}")

        print("\n")
        time.sleep(4)

        if enemy_total_health < 1:
            print(f"{hero["name"]} ganhou o combate")
            break


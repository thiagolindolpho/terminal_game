import random
import time
from calculate_dmg import calculate_damage
#(hero["damage"] - (hero["damage"] - 1))


def combat_start(hero, enemy):

    enemy_actual_health = enemy["health"]
    enemy_max_health = enemy["health"]
    hero_actual_health = hero["health"]
    hero_max_health = hero["health"]
    coin_flip = 0


    while True:
        coin_flip = random.randint(1, 2)

        if coin_flip == 1:
            enemy_actual_health -= calculate_damage(hero, enemy) # <-- calculo de dano vem aqui
        elif coin_flip == 2:
            hero_actual_health -= calculate_damage(enemy, hero)
        
        if enemy_actual_health < 1:
            print(f"\n{hero["name"]} was victorious")
            break
        elif hero_actual_health < 1:
            print(f"\n{enemy["name"]} killed {hero["name"]}!")
            break
       

        if coin_flip == 1:
            print(f"enemy current health: {enemy_max_health}/{enemy_actual_health}(-{calculate_damage(hero, enemy)})")
        elif coin_flip == 2:
            print(f"hero current health: {hero_max_health}/{hero_actual_health}(-{calculate_damage(enemy, hero)})")
        else:
            print("ERROR")
            break

        print("\n")
        time.sleep(4)

        

import random
import time
from calculate_dmg import calculate_damage


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
       
        #é preciso implementar as funções para o roubo de vida e a regeneração de vida
        #ambos não podem curar acima da vida maxima do heroi, isso seria aumentar a vida maxima e não curar
        if coin_flip == 1:
            print(f"{hero["name"]} unleashes x{hero["attack_speed"] // 5} attacks, inflicting {calculate_damage(hero, enemy)}.\n")
            print(f" - Damage reduced by enemy: {round((hero["attack_speed"] // 5 * (enemy["armor"] / 3)))}")
            print(f" - Hero Health Regeneration: {hero["health_regen"]}")
            print(f" - Hero Lifesteal: {hero["life_steal"]}\n")
            print(f"enemy current health: {enemy_max_health}/{enemy_actual_health}(-{calculate_damage(hero, enemy)})")
        elif coin_flip == 2:
            print(f"{enemy["name"]} attacks {hero["name"]}, inflicting {calculate_damage(enemy, hero)}.")
            print(f"hero current health: {hero_max_health}/{hero_actual_health}(-{calculate_damage(enemy, hero)})")
            #falta colocar o dano reduzido pelo heroi aqui
        else:
            print("ERROR")
            break

        print("\n")
        time.sleep(4)

        

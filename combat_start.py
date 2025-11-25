import random
import time
from calculate_dmg import calculate_damage
from life_steal import life_steal
from health_regen import health_regen
from level_up import level_up


def combat_start(hero, enemy):

    enemy_actual_health = enemy["health"]
    enemy_max_health = enemy["health"]
    hero_actual_health = hero["health"]
    hero_max_health = hero["health"]
    life_steal_cure = 0
    health_regen_cure = 0
    
    
    coin_flip = 0


    while True:
        coin_flip = random.randint(1, 2)

        if coin_flip == 1:
            enemy_actual_health -= calculate_damage(hero, enemy)
            life_steal_cure = life_steal(hero, hero_actual_health)
            health_regen_cure = health_regen(hero, hero_actual_health)
            hero_actual_health += life_steal_cure
            hero_actual_health += health_regen_cure 
        elif coin_flip == 2:
            hero_actual_health -= calculate_damage(enemy, hero)
            health_regen_cure = health_regen(hero, hero_actual_health)
            hero_actual_health += health_regen_cure
        
        if enemy_actual_health < 1:
            print(f"\n{hero["name"]} was victorious\n")

            return level_up(hero, enemy)

            break
        elif hero_actual_health < 1:
            print(f"\n{enemy["name"]} killed {hero["name"]}!")
            break
       
        
        if coin_flip == 1:
            print(f"{hero["name"]} unleashes x{hero["attack_speed"] // 5} attacks, inflicting {calculate_damage(hero, enemy)} damage.\n")
            print(f" - Damage reduced by enemy: {round((hero["attack_speed"] // 5 * (enemy["armor"] / 3)))}")
            print(f" - Hero Health Regeneration: +{health_regen_cure}")
            print(f" - Hero Lifesteal: +{life_steal_cure}\n")
            print(f"enemy current health: {enemy_max_health}/{enemy_actual_health}(-{calculate_damage(hero, enemy)})")
        elif coin_flip == 2:
            print(f"{enemy["name"]} attacks {hero["name"]}, inflicting {calculate_damage(enemy, hero)} damage.\n")
            print(f" - Damage reduced by hero: {round((hero["armor"] / 3))}")
            print(f" - Hero Health Regeneration: +{hero["health_regen"]}\n")
            print(f"hero current health: {hero_max_health}/{hero_actual_health}(-{calculate_damage(enemy, hero)}) hp regen: (+{health_regen_cure})")
        else:
            print("ERROR")
            break
    
    #proximo passo é criar função de subir de nivel que acumula e checa se a xp é o sufuiciente para subir de nivel e se for, aumentar os atributos

        print("\n")
        time.sleep(4)

        

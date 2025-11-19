from rand_enemy import enemy_randomizer
from run_or_fight import run_or_fight


def encounter(enemy_list, hero):
    print("\n" + "!" * 10 + "  ENCOUNTER  " + "!" * 10)
    hero1 = hero
    random_enemy = enemy_randomizer(enemy_list)

    print(f"\n    a {random_enemy["name"]} appears!")
    print()
        
    # Breve descrição da ação
    print(f"    The {random_enemy["name"]} rush into attack, closing the distance quickly.")
    print("    Kaelen raises his guard. There is no time for dialogue.")
    print()

    print(" - type 1 for fight\n - type 2 for escape")
    escolha = input("\n > input: ")

    run_or_fight(escolha, hero, random_enemy)
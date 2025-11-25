import os
from escape_combat import escape_combat
from combat_start import combat_start



def run_or_fight(escolha, hero, enemy):
    while True:
            if escolha == "1":
                return combat_start(hero, enemy)
                break
            elif escolha == "2":
                escape_combat()
                break
            else:
                os.system('clear')
                print(" ERROR\n")
                print(" - type 1 for fight\n")
                print(" - type 2 for escape\n")

                escolha = input(" > input: ")
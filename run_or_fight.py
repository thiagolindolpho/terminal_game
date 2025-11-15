import os
from escape_combat import escape_combat

def run_or_fight(escolha):
    while True:
            if escolha == "1":
                #combat_start()
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
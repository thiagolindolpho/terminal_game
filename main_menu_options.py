from game_start import start_game
import os

def options(escolha):
    while True:
        if escolha == "1":
            start_game()
            break
        elif escolha == "2":
            break
        else:
            os.system('clear')
            print(" ERROR\n")
            print(" - type 1 for start\n")
            print(" - type 2 for quit\n")

            escolha = input(" > input: ")
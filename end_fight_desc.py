import random

# Lista de descrições de vitória
victory_description_list = [
    "\n    Kaelen stands triumphant over his defeated foe(s). He takes a moment to secure his gear.",
    "\n    With a final, decisive strike, Kaelen claimed the skirmish. He wipes his blade clean and presses on.",
    "\n    Combat concluded. The threat is neutralized, and Kaelen glances around the woods, confirming silence.",
    "\n    Kaelen sweeps his weapon clean. Victory secured, he continues his grim mission.",
    "\n    The brief fight is over. Kaelen pauses only long enough to check his surroundings before rejoining the path.",
    "\n    The air clears of the threat. Kaelen was victorious and now resumes his journey through the dense woods."
]

def combat_victory():
    # Calcula o número aleatório para acessar a lista (como na sua estrutura original)
    random_number = random.randint(0, len(victory_description_list) - 1)
    
    # Imprime a mensagem escolhida (como você solicitou)
    print(victory_description_list[random_number])
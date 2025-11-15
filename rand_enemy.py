import random

def enemy_randomizer(enemy_list):
    random_index= random.randint(0, len(enemy_list) - 1)

    random_enemy= enemy_list[random_index]

    return random_enemy
import random

def item_randomizer(item_list):
    random_index= random.randint(0, len(item_list) - 1)

    random_item = item_list[random_index]

    return random_item
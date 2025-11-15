import random
from items import item_list

def item_randomizer():
    random_index= random.randint(0, len(item_list) - 1)

    random_item = item_list[random_index]

    return random_item
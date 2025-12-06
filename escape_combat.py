import random

escape_description_list = [
    "\n    Kaelen deemed the fight unnecessary. He escaped.",
    "\n    Kaelen did not fight. He focused only on speed, slipping past the enemies.",
    "\n    A quick, tactical retreat. Kaelen's training allowed him to run away."

]

random_number = random.randint(0, len(escape_description_list) - 1)

def escape_combat():
    
    print(escape_description_list[random_number])


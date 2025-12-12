import random

escape_description_list = [
    "\n    Kaelen deemed the fight unnecessary. He escaped.",
    "\n    Kaelen did not fight. He focused only on speed, slipping past the enemies.",
    "\n    A quick, tactical retreat. Kaelen's training allowed him to run away."

]

def escape_combat():
    random_number = random.randint(0, len(escape_description_list) - 1)
    
    print(escape_description_list[random_number])


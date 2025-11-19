def calculate_damage(attacker, receptor):
    dmg_value = round(attacker["damage"] - (receptor["armor"] / 3))

    return dmg_value


    

        

    
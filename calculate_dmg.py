def calculate_damage(attacker, receptor):
    if attacker["type"] == "hero":
        dmg_value = round((attacker["damage"] * (attacker["attack_speed"] // 5)) - (attacker["attack_speed"] // 5 * (receptor["armor"] / 3)))
    else:
        dmg_value = round(attacker["damage"] - (receptor["armor"] / 3))

    return dmg_value


    

        

    
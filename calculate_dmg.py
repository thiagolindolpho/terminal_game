def calculate_damage(attacker, receptor):
    new_health = round(receptor["health"] - (attacker["damage"] - (receptor["armor"] / 3)))

    return new_health


    #na hora do loop do combat_start a vida não está diminuindo

        

    
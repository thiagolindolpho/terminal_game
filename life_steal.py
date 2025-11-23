def life_steal(attacker, current_health):
    
    if (attacker["life_steal"] + current_health) >= attacker["health"]:
        return attacker["health"] - current_health
    else:
        return attacker["life_steal"]
        

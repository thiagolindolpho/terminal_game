def health_regen(hero, current_health):
    
    if (hero["health_regen"] + current_health) >= hero["health"]:
        return hero["health"] - current_health
    else:
        return hero["health_regen"]
xp = 0

def level_up(hero, enemy, current_health):
    if (enemy["xp"] + hero["current_xp"]) > hero["xp_bar"]:
        hero["health"] += 10
        hero["current_health"] = current_health
        hero["health_regen"] += 1
        hero["damage"] += 5
        hero["armor"] += 2
        hero["magic_resistance"] += 1
        hero["attack_speed"] += 1
        hero["current_xp"] = (enemy["xp"] + hero["current_xp"]) - hero["xp_bar"]
        hero["xp_bar"] += round(hero["xp_bar"] / 3)
        hero["level"] += 1

        print(f"{hero["name"]} leveled-up!")

        while hero["current_xp"] >= hero["xp_bar"]:
            hero["health"] += 10
            hero["current_health"] = current_health
            hero["health_regen"] += 1
            hero["damage"] += 5
            hero["armor"] += 2
            hero["magic_resistance"] += 1
            hero["attack_speed"] += 1
            hero["current_xp"] = (hero["current_xp"]) - hero["xp_bar"]
            hero["xp_bar"] += round(hero["xp_bar"] / 3)
            hero["level"] += 1

            print(f"{hero["name"]} leveled-up!")

        return hero
    elif (enemy["xp"] + hero["current_xp"]) == hero["xp_bar"]:
        hero["health"] += 10
        hero["current_health"] = current_health
        hero["health_regen"] += 1
        hero["damage"] += 5
        hero["armor"] += 2
        hero["magic_resistance"] += 1
        hero["attack_speed"] += 1
        hero["current_xp"] = 0
        hero["xp_bar"] += round(hero["xp_bar"] / 3)
        hero["level"] += 1

        print(f"{hero["name"]} leveled-up!")

        return hero
    else:
        print(f"{hero["name"]} gained {enemy["xp"]}XP!")

        hero["current_health"] = current_health
        hero["current_xp"] += enemy["xp"]

        return hero
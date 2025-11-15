def equip_item(hero, item):
    for chave, valor in item.items():
        hero_chave = list(hero.keys())

        for c in hero_chave:
            if chave == c and c != "name":
                hero[chave] += valor

    return hero
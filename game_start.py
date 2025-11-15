from rand_item import item_randomizer
from rand_enemy import enemy_randomizer
from equip_item import equip_item
from enemies import enemy_list1, enemy_list2, enemy_list3
from hero import hero
import os
from run_or_fight import run_or_fight


def start_game():
    print("\n   game started!\n")

    print("\n" + "*" * 60)
    print("                *** INTRODUCTION ***")
    print("*" * 60)
    print("\n")

    SPECIAL_ITEM = item_randomizer()
    hero_kaelen = None
    escolha = None
    random_enemy = None

    # Início da Narrativa
    print("    The air in the capital of Aldoria was thick with despair, a heavy blanket of grief")
    print("    woven into the usually cheerful banners that now hung limp from the castle turrets.")
    print("    The heart of the kingdom, the luminous Princess Lyra, had vanished.")
    print() # Linha vazia

    print("    You, Kaelen, are a sellsword of renown—a warrior whose reputation for skill")
    print("    and discretion stretches far beyond the muddy borders of the provinces.")
    print("    You had been resting in the small, unassuming tavern of The Drunken Stag,")
    print("    enjoying the hard-earned quiet, when the summons came.")
    print() # Linha vazia

    print("    A Royal Guard, clad in the silver and blue of the Aldorian family crest,")
    print("    strode into the tavern, his face etched with urgency. The room fell silent as he")
    print("    approached your table, drawing all eyes to the solitary figure of the celebrated mercenary.")
    print() # Linha vazia

    print('    "Kaelen," the Guard stated, his voice ringing with formal authority despite the')
    print('    sweat on his brow, "His Royal Majesty, King Alaric, requests your presence.')
    print('    Immediately. This is a matter of the highest national peril."')

    input("\n > press any key")
    os.system("clear")

    # A Cena do Rei
    # O separador é mantido centralizado na borda do terminal (sem recuo)
    print("\n" + "=" * 20 + " The King's Distress " + "=" * 20)

    print("    Within the echoing silence of the Throne Room, King Alaric paced before his golden seat.")
    print("    He was a man accustomed to command, but today, his eyes held the haunted look of a father.")
    print("    He dismissed his advisors with a wave and turned to you, his voice low and tight.")
    print() # Linha vazia

    print('    "Kaelen. It is as the rumours say, and yet worse. My daughter, Princess Lyra,')
    print('    has been taken. Torn from her bed in the dead of night." The King gestured to a small,')
    print('    dark object on a nearby velvet cushion—a scale, jet black and sharp as a dagger.')
    print() # Linha vazia

    print('    "This was all they left. It is the foul signature of Lord Malakor."')

    # Explicação do Vilão
    print("\n" + "    > Note: Lord Malakor is a powerful sorcerer and self-proclaimed") # Recuo no início do texto
    print("    Dragon-Lord who seeks to use the royal bloodline to unlock a dark, forgotten power.")

    # A Missão
    print("    His lair is somewhere in the Blackspine Mountains," + ' the King continued, his gaze piercing.')
    print('    "A journey of immense danger. My own armies would take weeks to mobilise, and by then, it may be too late..."')
    print() # Linha vazia

    print(f'   I offer you "{SPECIAL_ITEM["name"]}" that will help you') # Recuo e variável corrigida
    print("    beyond your wildest dreams—and a noble title, should you succeed.")
    print("    But more important than coin or rank, Kaelen, you would save the heart of our kingdom. Bring my Lyra home.")
    print() # Linha vazia

    print("    You accept the King’s charge. Your adventure begins not with a parade, but with a lone,")
    print("    grim departure from the castle gates, your weapon on your back and the unsettling")
    print("    image of the black dragon scale burned into your memory. The road to the Blackspine")
    print("    Mountains is long and perilous, riddled with Malakor’s dark influence.")
    print() # Linha vazia

    print("    The fate of Princess Lyra, and perhaps the realm of Aldoria itself, now rests entirely upon the strength and cunning of Kaelen.")

    # O rodapé é mantido centralizado na borda do terminal (sem recuo)
    print("\n" + "*" * 60)
    print("                *** END OF INTRODUCTION ***")
    print("*" * 60)

    hero_kaelen = equip_item(hero, SPECIAL_ITEM)

    print(hero_kaelen)

    input("\n > press any key")
    os.system("clear")
    print("\n" + "=" * 10 + "  WHISPERING WOODS  " + "=" * 10)

    # A nova introdução foca na transição e no peso da missão
    print("    Kaelen wasted no time. The black dragon scale, a promise of terror, felt cold")
    print("    in his pouch. He passed the weeping crowds at the gates of Aldoria and soon")
    print("    left the paved roads, turning onto the narrow, overgrown hunting trails.")
    print()

    print("    The kingdom's fields gave way quickly to the dense woods—the **Whispering Woods**.")
    print("    Here, the sunlight died, and the royal urgency was replaced by the silence of the hunt.")

    input("\n > press any key")
    os.system("clear")
    print("\n" + "!" * 10 + "  ENCOUNTER  " + "!" * 10)
    random_enemy = enemy_randomizer(enemy_list1)

    print(f"\n    a group of {random_enemy["name"]} appears!")
    print()
    
    # Breve descrição da ação
    print(f"    The group of {random_enemy["name"]} rush into attack, closing the distance quickly.")
    print("    Kaelen raises his guard. There is no time for dialogue.")
    print()

    print(" - type 1 for fight\n - type 2 for escape")
    escolha = input("\n > input: ")

    run_or_fight(escolha)
    
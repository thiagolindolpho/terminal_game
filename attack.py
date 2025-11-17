import time

#ERRO AQUI

#função não se comporta como deveria, break nunca é alcançado 
#a cada loop a vida do inimigo reseta, o dano na vida não acumula
#vida chega em valor negativo mas o break não ativa


def attack(attacker, receiver):
    receiver_total_health = receiver["health"]
    receiver_max_health = receiver["health"]

    while True:
        receiver_total_health -= attacker["damage"]

        print(f"enemy total health: {receiver_max_health}")
        print(f"enemy_health: {receiver_max_health} - hero_dmg: {attacker["damage"]}")
        print(f"enemy atual health: {receiver_total_health}")
        print("\n")
        time.sleep(2)

        if receiver_total_health < 0:
            break

        

    
import random

def finalBossBattle():
    boss_name = "Sephiroth"
    boss_health = 1000000
    attacks = {
        "octoslash": 300,
        "gigaflare": 430,
        "supernova": 580
    }

    print(f"{boss_name} is preparing to attack!")
    while boss_health > 0:
        attack_name = random.choice(list(attacks.keys()))
        damage = attacks[attack_name]
        print(f"{boss_name} used {attack_name} and dealt {damage} damage!")
        player_health -= damage
        if player_health <= 0:
            print("You have been defeated!")
            break
        else:
            print(f"You took {damage} damage and have {player_health} health left.")
            print(f"{boss_name} has {boss_health} health left.")

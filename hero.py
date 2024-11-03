#reguli:1. doua zaruri per aruncare
#       2. zarurile cu suma cea mai mare castiga
#       3. uhhh... cam atat actually XD
#2 or more players allowed  (done)
#virtual wallet
#no money = no play
#no money left = kicked
#access to visualise your money
#the biggest score = win  (in progress)
#!!!LET THE GAME BEGIN!!!

import random

players = int(input("Cati jucatori participa?: "))
if players < 2:
    print("Trebuie sa fie minim 2 jucatori!")
    exit()
else:
    scores = {}

for i in range(1, players + 1):
    response = input(f"Jucator {i}, doresti sa participi? (da/nu): ").lower()
    if response == "da":
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        total = zar1 + zar2
        scores[f"Jucător {i}"] = total
        print(f"Jucatorul {i} a aruncat zarurile({zar1}, {zar2}) - Total: {total}!")

    elif response == "nu":
        print(f"Jucătorul {i} a ales să nu participe!")

    else:
        print(f"Opțiune invalidă, jucatorul {i} nu va participa!!")


if scores:
    jucator_castigator = max(scores, key=scores.get)
    scor_maxim = scores[jucator_castigator]

    print(f"Castigatorul este: {jucator_castigator} cu scorul {scor_maxim}")
else:
    print("Niciun cavaler nu a fost curajos sa joace!")

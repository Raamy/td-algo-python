# Valeurs initiales :
pSeuil = 2.3
vSeuil = 7.41


# Fonction qui vérifie les valeurs
def checking_room_values(v, p):
    if p > pSeuil and v > vSeuil:
        print("Arrêt immédiat.")
    elif p > pSeuil:
        print("Augmenter le volume svp.")
    elif v > vSeuil:
        print("Diminuer le volume.")
    else:
        print("Rien à signaler.")


pression = float(input("Entrez la pression : "))
volume = float(input("Entrez le volume courant : "))

checking_room_values(volume, pression)

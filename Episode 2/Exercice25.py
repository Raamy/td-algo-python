# Fonction qui renvoie la somme de 3 nombres
def somme(v1, v2, v3):
    return v1 + v2 + v3

nombre1 = int(input("Entrez le nombre n°1 : "))
nombre2 = int(input("Entrez le nombre n°2 : "))
nombre3 = int(input("Entrez le nombre n°3 : "))

tuples = (nombre1, nombre2, nombre3)
print(somme(tuples))

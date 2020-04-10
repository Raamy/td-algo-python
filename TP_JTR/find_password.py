import hashlib
import re

# --------------- #
# Contient la liste des animaux
liste_animaux = []

# Contient la liste des noms
liste_noms = []

# Contient la liste des prénoms
liste_prenoms = []

# Contient la liste des mots de passe cryptés
liste_passwords = []

# Contient la liste des mots de passe non-cryptés
liste_clear_passwords = []

# Contient la liste des résultats (Nom, prénom et mot de passe en clair)
resultats = []

# Fichier contenant la liste des résultats
file_resultats = open("resultats.txt", "w+", encoding="utf-8")
# ---------------- #

# Retourne (dans une liste) le mot de passe de chaque ligne du tableau CSV
def get_only_password(line):
    line = line.replace(";;;;;", "").rstrip()
    liste_test = [pos for pos, char in enumerate(line) if char == ";"]
    return line[liste_test[1] + 1:len(line)]


# Retourne un bool en fonction de la validité du mot de passe
def check_password(clear_password, password):
    result = hashlib.md5(str.encode(clear_password))
    result = result.hexdigest()
    if result == password:
        return True


# Retourne les noms de familles présent dans la liste CSV
def get_only_surnames(line):
    liste_test = [pos for pos, char in enumerate(line) if char == ";"]
    return line[liste_test[0]:liste_test[1]].replace(";", "")


def add_clear_password(clear_password, index):
    print(liste_noms[index] + " " + liste_prenoms[index] + ", Mot de passe : " + clear_password)
    file_resultats.write(liste_noms[index] + " " + liste_prenoms[index] + ", Mot de passe : " + clear_password + "\n")


def replace_vowels_with_numbers(string):
    list_try = [0, 0, 0, 0, 0]
    liste_voyelle = ['a', 'e', 'i', 'o', 'u', 'y']


# Lis le dictionnaire des animaux
# puis ajoute les animaux dans la liste des animaux
file_dico = open("dico_animaux.txt", "r", encoding="utf-8")
dico_animaux = file_dico.readlines()
for animaux in dico_animaux:
    liste_animaux.append(animaux.rstrip("\n\r"))

# Lis le fichier CSV : Nom ; Prénom ; Mot de passe cryptés
# Puis ajoute les noms, prénoms et mots de passes dans leurs listes respectives
file_passwords = open("Liste_Atrouver.csv", "r", encoding="utf-8")
passwords = file_passwords.readlines()
del passwords[0]
for line in passwords:
    liste_noms.append(get_only_surnames(line))
    liste_prenoms.append(re.sub(r';[^;]+', '', line.replace(";;;;;", "")))
    liste_passwords.append(get_only_password(line))

# print(liste_animaux)
# print(liste_noms)
# print(liste_prenoms)
# print(liste_passwords)

for animal in liste_animaux:
    clear_password1 = animal[::-1] + animal
    clear_password2 = animal
    # print(clear_password2)
    for password in liste_passwords:
        # print(password)
        print(add_clear_password(clear_password1, int(liste_passwords.index(password)))) if check_password(
            clear_password1, password) else None
        print(add_clear_password(clear_password2, int(liste_passwords.index(password)))) if check_password(
            clear_password2, password) else None

for nom in liste_noms:
    prenom = liste_prenoms[liste_noms.index(nom)].lower()
    clear_password1 = prenom[::-1]

    # print(clear_password1)
    # print(clear_password1)
    for password in liste_passwords:
        print(add_clear_password(clear_password1, int(liste_passwords.index(password)))) if check_password(
            clear_password1, password) else None

        # print(password)

for prenom in liste_prenoms:
    prenom = prenom.lower()
    for i in range(0, 9999):
        clear_password2 = prenom + str(i)
        if i <= 10:
            clear_password2 = prenom + "0" + str(i)
        # print(prenom + str(i))
        for password in liste_passwords:
            print(add_clear_password(clear_password2, int(liste_passwords.index(password)))) if check_password(
                clear_password2, password) else None

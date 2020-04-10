# Ecrire du code qui demande à l'utilisateur un nombre appelé x,
# le programme demandera alors x chaines de caractères que le programme enregistrera dans un fichier de nom data.txt
# (une chaine par ligne)

word_length = int(input("Bonjour, entrez un nombre : "))

word = str(input("Entrez un mot de longueur " + str(word_length) + " caractères : "))
while not(word_length == len(word)):
    word = str(input("Veuillez entrer un mot de longueur " + str(word_length) + " caractères : "))

file = open("Exercice21.txt", "a+")
file.write(word + "\n")
file.close()
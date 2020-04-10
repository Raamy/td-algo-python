# Vérifier si une chaine est un palindrome.

mot = str(input("Entrez un mot : "))

if mot == mot[::-1]:
    print("Ce mot est un palindrome.")
else:
    print("Ce mot n'est pas un palindrome.")
# Fonction qui vérifie l'addresse email :
def check_mail(address):
    mail_length = len(address)
    for char in address:
        if (char == '@') and address[len(address) - 4] == ".":
            print("Addresse mail valide")
            return True
    print("Addresse mail invalide")
    return False

file = open("Exercice21.txt", "r")
file1 = file.readlines()
for x in file1:
    # enlève le saut de ligne pour chaque ligne
    x = x.replace("\n", "")
    check_mail(x)

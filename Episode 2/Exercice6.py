# Fonction qui vérifie l'adresse mail :
def check_mail(address):
    for char in address:
        if (char == '@') and address.endswith(".com"):
            print("Addresse mail valide")
            return True
    print("Addresse mail invalide")
    return False

mail = str(input("Entrez une adresse mail : "))
check_mail(mail)

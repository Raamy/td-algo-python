# Vérifier si une chaine est un email en regardant la présence de @ et de . puis de max 3 caractères après le .

def check_mail(address):
    mail_length = len(address)
    for char in address:
        if (char == '@') and address[len(address) - 4] == ".":
            print("Addresse mail valide")
            return True
    print("Addresse mail invalide")
    return False

email = str(input("Entrez une addresse email : "))
check_mail(email)
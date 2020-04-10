import os.path
from os import path

file_name = str(input("Entrez le nom du fichier (avec l'extension) : "))



if path.exists(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line.replace("\\b\\", "")
        line.replace("\b\"", "")
        line.replace("\n", "")
        print(line)
else:
    print("Fichier non trouvé")
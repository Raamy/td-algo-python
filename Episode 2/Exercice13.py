# Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for et l’instruction range()

for number in range(0, 15):
    if (number % 2) != 0 and number != 0 and number != 15:
        print(number)
    number += 3

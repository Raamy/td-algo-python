# Utiliser une boucle while puis une boucle for pour afficher les n premiers nombres pairs.

number = 0

while number < 10:
    if (number % 2) == 0:
        print(number)
    number += 2

for number in range(10, 20):
    if (number % 2) == 0:
        print(number)
    number += 2
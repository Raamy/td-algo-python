liste = [17, 38, 10, 25, 72]

# triez et affichez la liste ;

liste.sort()
print(liste)

# ajoutez l’élément 12 à la liste et affichez la liste ;

liste.append(12)
print(liste)

# renversez et affichez la liste ;

liste.sort(reverse=True)
print(liste)

# affichez l’indice de l’élément 17 ;

print(liste.index(17))

# enlevez l’élément 38 et affichez la liste ;

liste.remove(38)
print(liste)

# affichez la sous-liste du 2e au 3e élément ;
print(liste[1:3])

# affichez la sous-liste du début au 2e élément ;
print(liste[0:2])

# affichez la sous-liste du 3e élément à la fin de la liste ;
print(liste[2:(len(liste))])

# affichez la sous-liste complète de la liste
print(liste[0:len(liste)])

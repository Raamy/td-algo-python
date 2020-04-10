def lexicographical_order(m1, m2):
    if m1 < m2:
        return m1
    else:
        return m2

mot1 = str(input("Entrez un premier mot : "))
mot2 = str(input("Entrez un deuxième mot : "))

print(lexicographical_order(mot1, mot2))
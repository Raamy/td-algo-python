def compterMots(words):
    words_list = words.split()
    result = {}
    for n in range(len(words_list)):
        result[n] = words_list[0]
    return result


mots = str(input("Entrez plusieurs mots : "))
print(compterMots(mots))

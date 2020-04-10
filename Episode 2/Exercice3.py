import math

def check_number(x):
    if x >= 0:
        print(str(math.sqrt(x)))
    else:
        return -1

number = float(input("Entrez un flottant : "))



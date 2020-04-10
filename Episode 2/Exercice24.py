from math import pi

def cube(x):
    return x*x*x

def volume_sphere(rayon):
    return ((4 * pi) * cube(rayon) / 3)

nombre = float(input("Entrez votre nombre : "))
print(volume_sphere(nombre))
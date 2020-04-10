# TP Python - John The Ripper

### Vous trouverez les résultats dans le fichier [resultat.txt](https://github.com/Raamy/td-algo-python/blob/master/TP_JTR/resultats.txt).

### Consigne :

John The Ripper (JTR) est un logiciel libre de cassage de mot de passe. Nous allons simuler ses attaques en Python
Il inclut l'auto-détection des tables de hachage utilisées par les mots de passe, l'implémentation d'un grand nombre d'algorithme de cassage, et autorise facilement l'implémentation de nouveaux algorithmes. 

John utilise 3 modes d'actions successivement :<br>
•	mode simple<br>
•	attaque par dictionnaire<br>
•	mode incrémental

Mode simple : des tests sont effectués à partir du nom de l'utilisateur auquel on fait subir des variantes Attaque par dictionnaire : des tests sont effectués à partir d'un fichier dictionnaire auquel on fait subir des variantes 
Mode incrémental: toutes les combinaisons sont testées -> très long...

Récupérez les 3 fichiers intéressants : Liste_Atrouver.xlsx, dico_animaux.txt 
Le premier contient 10 mots de passe, chiffré en MD5, l'autre des noms d'animaux 


### Votre objectif : trouvez le plus de mots de passe.

## L'éxecution de ce script inscrit les mot de passe dans le fichier resultat.txt.

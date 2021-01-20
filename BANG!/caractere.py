from random import *
import random


caract = ["Bart Cassidy",
"Kit Carlson",
"Black Jack", 
"Lucky Duke", 
"Calamity Janet",
"Paul Regret pv:3",
"El Gringo pv:3",
"Pedro Ramirez",
"Jesse Jones", 
"Rose Doolan",
"Jourdonnais",
"Sid Ketchum",
"Slab le flingueur",
"Sam le vautour",
"Suzy Lafayette",
"Willy le Kid"]


random.shuffle(caract)
print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")
print(sample(caract,4))
print("\n")

start = input("Quel carte choissez-vous ?""\n")
#if input is not in sample
print("error")
if str=="Sam le vautour":
        print("Tu es Sam le vautour, dès qu’un personnage est éliminé de la partie, Sam prend toutes les cartes que ce joueur avait en main et en jeu, et il les ajoute à sa propre main. Tu as 4 points de vies !") 
        exit()

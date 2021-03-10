from random import *
import random

finalcaract = []

caract = ["Bart Cassidy pv:4",
"Kit Carlson pv:4",
"Black Jack pv:4", 
"Lucky Duke pv:4", 
"Calamity Janet pv:4",
"Paul Regret pv:3",
"El Gringo pv:3",
"Pedro Ramirez pv:4",
"Jesse Jones pv:4", 
"Rose Doolan pv:4",
"Jourdonnais pv:4",
"Sid Ketchum pv:4",
"Slab le flingueur pv:4",
"Sam le vautour pv:4",
"Suzy Lafayette pv:4",
"Willy le Kid pv:4"]



def perso():

    random.shuffle(caract)

    # We ask that as long as there are more than 12 elements in the array you copy and delete one element and then put it in a second array.
    while (len(caract) > 12):
        selectrole = caract.pop()
        finalcaract.append(selectrole)
        
    print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")
    
    print(finalcaract)    

    startcaract = input("Quel carte choissez-vous ?")
    selectrole = caract.pop() # Récupère et supprime le dernier élément de la liste
        
    print("Voici ton rôle :")

    if startcaract == "1":
        print(finalcaract[0])
    if startcaract == "2":
        print(finalcaract[1])
    if startcaract == "3":
        print(finalcaract[2])
    elif startcaract == "4":
        print(finalcaract[3])
    
    print("\n")



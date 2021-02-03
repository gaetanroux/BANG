from random import *
import random


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
    print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")
    print(sample(caract,4))
    print("\n")

    start = input("Quel carte choissez-vous ?")
    SelectRole = caract.pop() # Récupère et supprime le dernier élément de la liste
    

    desc(SelectRole)

def desc(SelectRole):
    if int(SelectRole) == 1:
        print ("Voici ton role : oui")
    
   # if SelectRole == caract 2
    #print ("Voici ton role :"caract,2)

        
    print("\n")
#if int(start) == "Sam le vautour":
 #       print("Tu es Sam le vautour tu vas devoir ") 
 #       exit()


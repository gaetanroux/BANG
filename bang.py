import random


carte = ["Bandit", "Renégat", "Shérif", "Bandit"]


random.shuffle(carte) # Mélange les cartes
print("Les cartes sont mélangées voici les rôles :")
print(carte) # Affiche la liste mélanger

SelectRole = carte.pop()
print('Voici ton rôle :', SelectRole)


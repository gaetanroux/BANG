

def debutgame(carte):

    
    start = input("Combien de joueur êtes vous :")

    if int(start) < 4:
        print("Vous n'êtes pas assez pour lancer une partie (4 minimum).") 
        exit()
    
    if int(start) == 4:
        print("Vous êtes pile le nombre pour lancer une partie !\n")
        

    if int(start) == 5:
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, une carte supplémentaire s'ajoute.\n")
       


    if int(start) == 6:
        carte.append("Hors-la-loi")
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, deux cartes supplémentaires s'ajoute.\n")
      



    if int(start) == 7:
        carte.append("Adjoint")
        carte.append("Hors-la-loi")
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, trois cartes supplémentaires s'ajoute.\n")
      

        
print("La partie commence...\n")

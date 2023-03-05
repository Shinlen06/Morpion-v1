def dessine(plateau):
    for ligne in plateau:
        print()
        for case in ligne:
            if case == 0:
                print(" ", end="")
            elif case == 1:
                print("O", end="")
            elif case == 2:
                print("X", end="")
            print("|", end="")
    print("")       


plateau = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

joueur = 1
partie_continue = True
while partie_continue:
    dessine(plateau)
    ligne = input("Fais le choix de la ligne entre 0 et 2 : ")
    colonne = input("Fais le choix de la colonne entre 0 et 2 : ")
    l = int(ligne)
    c = int(colonne)
    if c >= 0 and l >= 0:
        if c < 3 and l < 3:
            if plateau[l][c] == 0:
                plateau[l][c] = joueur
                if plateau[l][0] == plateau[l][1] == plateau[l][2] != 0:
                    print("Joueur vainqueur : ", joueur)
                    dessine(plateau)
                    partie_continue = False
                if plateau[0][c] == plateau[1][c] == plateau[2][c] != 0:
                    print("Joueur vainqueur : ", joueur)
                    dessine(plateau)
                    partie_continue = False
                if plateau[0][0] == plateau[1][1] == plateau[2][2] != 0:
                    print("Joueur vainqueur : ", joueur)
                    dessine(plateau)
                    partie_continue = False
                if plateau[0][2] == plateau[1][1] == plateau[2][0] != 0:
                    print("Joueur vainqueur : ", joueur)
                    dessine(plateau)
                    partie_continue = False        
                    
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1

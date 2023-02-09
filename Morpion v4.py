plateau = [[-1, 1, 1],
           [-1, 0, 0],
           [1, -1, 1]]

partie_continue = True
while partie_continue:
    for ligne in plateau:
        print()
        for case in ligne:
            if case == -1:
                print(" ", end="")
            elif case == 0:
                print("O", end="")
            elif case == 1:
                print("X", end="")
            print("|", end="")
    print("")       
    ligne = input("Fais le choix de la ligne entre 0 et 2 : ")
    colonne = input("Fais le choix de la colonne entre 0 et 2 : ")
        
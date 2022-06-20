from random import*
from random import randint
import combat

player = "Player"
monster = "monster"
inventory = "trésor "

L = []

def Player():
    X = 0
    Y = 0
    player = "Joueur"
    L[X][Y] = player
    print(L[0])
    print(L[1])
    
    for loop in range(500):
        x = input()

        if L[0][24] == player or L[1][24] == player:
            print("Fin du jeu")
            return

        if L[X][Y + 1] == monster and x == "d":
            print("Vous affrontez un monstre !")
            

        elif L[0][Y] == monster and x == "z":
            print("Vous affrontez un monstre !")

        elif L[X][Y + 1] == inventory and x == "d":
            print("Vous avez trouvé un trésor !")

        elif L[1][Y] == inventory and x == "s":
            print("Vous avez trouvé un trésor !")

        i = 0
        while i < len(L[0])-1:
            if x == "z" and L[0][i] == player:
                L[0][i] = player
                print(L[0])
                print(L[1])
                X = 0
                Y = i
            i = i + 1

        if x == "z":
            while X == 1:
                X = X - 1
                Y = Y
                L[X][Y] = player
                L[X - 1][Y] = "_"
                print(L[0])
                print(L[1])

        i = 0
        while i < len(L[1])-1:
            if x == "s" and L[1][i] == player:
                L[1][i] = player
                print(L[0])
                print(L[1])
                X = 1
                Y = i
            i = i + 1

        if x == "s":
            while X < 1:
                X = X + 1
                Y = Y
                L[X][Y] = player
                L[X - 1][Y] = "_"
                print(L[0])
                print(L[1])

        elif x == "d":
            X = X
            Y = Y + 1
            L[X][Y] = player
            L[X][Y - 1] = "_"
            print(L[0])
            print(L[1])

        elif x == "q" and L[0][0] == player:
            L[0][0] = player
            print(L[0])
            print(L[1])

        elif x == "q" and L[1][0] == player:
            L[1][0] = player
            print(L[0])
            print(L[1])

        elif x == "q":
            X = X
            Y = Y - 1
            L[X][Y] = player
            L[X][Y + 1] = "_"
            print(L[0])
            print(L[1])

def map(player, monster, inventory):
    print("Tapez m pour ouvir la map")
    print("Tapez z pour aller en haut")
    print("Tapez s pour aller en bas")
    print("Tapez d pour aller à droite")
    print("Tapez q pour aller à gauche")
    x = input()
    while x != "m":
        x = input()
    if x == "m":
        
        a = 0
        while a < 2:
            l = []
            b = 0
            while b < 25:
                l.append("_")
                b = b + 1
            L.append(l)
            a = a + 1

        for loop in range(3):
            L[0][randint(0,len(L[0])-1)] = monster
            L[1][randint(0,len(L[1])-1)] = inventory

        Player()

        return(L)

map(player, monster, inventory)
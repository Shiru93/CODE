'''
Mini projet - Créer un jeu de pendu. le jeu commence par un petit menu dans lequel le joueur peut choisir la difficulté de sa partie, 
ensuite un mot sera choisi aléatoirement parmi plusieurs de mots liés à la difficulté (facile : mot de 4 lettres, moyen : 6 lettres, difficile : 8 lettres). 
Une fois le mot choisi, le jeu se lance et affiche le nombre de lettres du mot caché. Le jeu proposera au joueur de deviner une des lettres du mot, 
si le joueur tombe juste, elle se dévoile et montre son emplacement dans le mot, 
si le joueur se trompe une partie du pendu s'affiche et enfin si le joueur propose une lettre qui a déjà été proposé rien ne se passe. 
Le jeu se termine lorsque toutes les lettres du mot sont affichées ou bien lorsque le joueur n'a plus d'essais et donc que le pendu est complet. 
Quelque soit la fin, le menu se relance pour pouvoir faire une nouvelle partie.
'''
import random

print("Quel est la difficulté choisie ?")
print("")
print("Tapez 1 : difficulté Facile")
print("Tapez 2 : difficulté Moyen")
print("Tapez 3 : difficulté Difficile")
print("")
x = int(input())
print(x)

def mot_random(mot):
    return random.choice(mot)


L = []
Mot = []

def Lettre(L):
    lettre = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    secret_word = mot_random(L)
    i = 0
    while i < len(secret_word):
        Mot.append("_")
        i = i + 1 
    print(Mot)
    nb_esay = 0
    while nb_esay < 7 and Mot != list(secret_word):
        l = input("Veuillez entrer une lettre : ",)
        i = 0
        is_choice_in_word = False
        while len(l) > 1 and l not in lettre:
            print("Veillez retaper votre lettre : ",)
            l = input()
        while i < len(secret_word):
            if secret_word[i] == l:
                Mot[i] = l
                is_choice_in_word = True
            i = i + 1
            
        if not is_choice_in_word:
            nb_esay = nb_esay + 1

        print(Mot)
        print("Il vous reste", 7 - nb_esay, "chance(s)")

        if Mot == list(secret_word):
            print("Bien joué")
        elif l not in Mot:
            print("T'as perdu")
            


def Facile(L):
    if x == 1:
        print("Vous avez choisis la difficulté Facile")
        L.append("mort")
        L.append("fuir")
        L.append("saut")
        L.append("gars")
        print(Lettre(L))

def Moyen(L):
    if x == 2:
        print("Vous avez choisis la difficulté Moyen")
        L.append("anales")
        L.append("ablata")
        L.append("enzyme")
        L.append("noyeau")
        L.append("propre")
        L.append("abysse")
        print(Lettre(L))

def Difficile(L):
    if x == 3:
        print("Vous avez choisis la difficulté Difficile")
        L.append("ambiante")
        L.append("affolant")
        L.append("évanouie")
        L.append("typhoses")
        L.append("abstenue")
        L.append("achetant")
        L.append("abjectes")
        L.append("abominer")
        print(Lettre(L))

print(Facile(L))
print(Moyen(L))
print(Difficile(L))
        


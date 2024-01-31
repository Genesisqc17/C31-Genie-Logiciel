import this

# all functions in python return something. if you don't ask it to return something it returns none (null)
# Valeurs sont typees mais ils n'ont pas besoin d'etre declarer (int, string, etc)

# Commentaire pour Entree/Sortie

# entree
# valeur = input("Ecrivez votre choix ici: ")

# transtypage en int
# valeur2 = int(input("Ecrivez combien: "))
# valeur2 = str(valeur2)
# transforme la valeur(chaine) en integer
# valeur3 = valeur2**valeur2 # ** = puissance
# exposant valeur2

# sortie
# print("Hello World!!!", valeur, valeur+valeur2) #, valeur3) # on peut mettre autant de valeur d'affiler separer d'une virgule

# mafonction ne peut pas etre utiliser avant d'etre defini
# python fonction ligne apres ligne

# definition de fonction
def mafonction(val=1):  # no {} indentation block instead # (val=1) = valeur par defaut
    print(val)
    return "Ca bin marcher"
    # pass = placeholder


# valeur = mafonction()
# print(valeur)
maliste = [len("bleu poudre"), 1, 42.5, 3, 4] # len = length
for i in maliste: # python n'aime pas qu'on enleve des items de la liste durant le loop. Il faut alors garder une liste des items a enlever et les enlever apres le loop
    if i >= 3:
        mafonction(i)

#for i in range(5):  # range = nombre de loop i = variable quelquonque
#    mafonction(i)

## Animations dans python (sequence d'images) gif ne donne pas le nombre d'images. il faut une fonction qui donne le nombre d'image total

#dunder = double under
# namespace
# __name__ = "__main__"

# def function
# for i blabla
#   blabla
# if __name__ = "__main__"
#   c = controleur

# import code_corpo
# code_corpo.mafunction()
# or import code_corpo as cc
# cc.mafunction()

# from code_corpo import * (pour cas tres special)
# utiliser pour importer tkenter
import random


class Modele():
    def __init__(self, parent):  # function utiliser a la creation de l'objet sur l'objet
        self.parent = parent
        self.largeur = 10
        self.hauteur = 8
        self.doc = [random.randrange(self.largeur),
                    random.randrange(self.hauteur)]


# python creer un objet mm si il ne contient rien
# __init__(self) ajoute des attributs a l'interieur de l'objet deja cree
class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele

    def affiche_tableau(self):
        tableau = []
        for i in range(self.modele.hauteur):
            ligne = []
            for j in range(self.modele.largeur):
                ligne.append(" ")
            tableau.append(ligne)

        tableau[self.modele.doc[1]][self.modele.doc[0]] = "D"

        for i in tableau:
            print(i)


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.afficher_jeu()

    def afficher_jeu(self):
        self.vue.affiche_tableau()


if __name__ == "__main__":
    controleur = Controleur()

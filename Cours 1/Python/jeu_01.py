import random


class Modele():
    def __init__(self, parent):  # function utiliser a la creation de l'objet sur l'objet
        self.parent = parent
        self.largeur = 8
        self.hauteur = 6
        self.doc = Docteur(self)
        self.daleks = []
        self.dalek_par_nivo = 5
        self.nivo = 0
        self.creer_nivo()

    def creer_nivo(self):
        self.nivo += 1
        nb_daleks = self.dalek_par_nivo * self.nivo
        pos_possible = []
        while nb_daleks:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            if [x, y] != [self.doc.posX, self.doc.posY] and [x, y] not in pos_possible:
                pos_possible.append([x, y])
                nb_daleks -= 1
        for i in pos_possible:
            d = Daleks(self, i)
            self.daleks.append(d)

    def jouer_coup(self, modif):
        self.doc.deplacer(modif)


class Daleks():
    def __init__(self, parent, pos):
        self.parent = parent
        self.posX, self.posY = pos


class Docteur():
    def __init__(self, parent):
        self.parent = parent
        self.posX = random.randrange(self.parent.largeur)
        self.posY = random.randrange(self.parent.hauteur)

    def deplacer(self, modif):
        x, y = modif
        # NOTE eventuellement verifier les bordures
        self.posX += x
        self.posY += y


# python creer un objet mm si il ne contient rien
# __init__(self) ajoute des attributs a l'interieur de l'objet deja cree
class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.dico_deplacement = {"1": [-1, 1],
                                 "2": [0, 1],
                                 "3": [1, 1],
                                 "4": [-1, 0],
                                 "5": [0, 0],
                                 "6": [1, 0],
                                 "7": [-1, -1],
                                 "8": [0, -1],
                                 "9": [1, -1]
                                 }

    def afficher_menu_jeu(self):
        rep = input("Indiquez votre coup (clavier num.): ")
        rep_dep = self.dico_deplacement[rep]
        return rep_dep


    def affiche_tableau(self):
        tableau = []
        for i in range(self.modele.hauteur):
            ligne = []
            for j in range(self.modele.largeur):
                ligne.append(" ")
            tableau.append(ligne)

        tableau[self.modele.doc.posY][self.modele.doc.posX] = "D"
        for i in self.modele.daleks:
            tableau[i.posY][i.posX] = "W"

        for i in tableau:
            print(i)


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.afficher_jeu()
        self.jouer_partie()

    def jouer_partie(self):
        rep = self.vue.afficher_menu_jeu()
        reponse = self.modele.jouer_coup(rep)
        self.vue.affiche_tableau()
        self.jouer_partie()

    def afficher_jeu(self):
        self.vue.affiche_tableau()



if __name__ == "__main__":
    controleur = Controleur()

import random


class Modele():
    def __init__(self, parent):  # function utiliser a la creation de l'objet sur l'objet
        self.parent = parent
        self.largeur = 8
        self.hauteur = 6
        self.doc = Docteur(self)
        self.daleks = []
        self.dalek_par_nivo = 5
        self.tdf = []
        self.nivo = 0
        self.zap = 0
        self.creer_nivo()
        self.score = 0
        self.gameover = False

    def creer_nivo(self):
        self.tdf.clear()
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

        self.zap += 1

    def jouer_coup(self, modif):
        if modif == "t":
            self.doc.tp()
        elif modif == "z":
            self.zapper()
        else:
            self.doc.deplacer(modif)

    def dalek_move(self):
        for i in self.daleks:
            i.deplacer()

    def verif_collision(self):
        collisions = []
        for i in self.daleks:
            for j in self.daleks:
                if i != j and i.posX == j.posX and i.posY == j.posY:
                    if i not in collisions:
                        collisions.append(i)

        for i in self.daleks:
            if i.posX == self.doc.posX and i.posY == self.doc.posY:
                self.gameover = True

        for i in collisions:
            self.daleks.remove(i)

        for i in collisions:
            t = TasFerraille(self, [i.posX, i.posY])
            self.tdf.append(t)

        self.score += len(collisions) * 5

        collisions.clear()

        for i in self.daleks:
            for j in self.tdf:
                if i.posX == j.posX and i.posY == j.posY:
                    if i not in collisions:
                        collisions.append(i)

        for i in collisions:
            self.daleks.remove(i)

        self.score += len(collisions) * 5

    def zapper(self):
        morts = []
        for i in self.daleks:
            if self.doc.posX + 1 > i.posX > self.doc.posX - 1:
                if self.doc.posY + 1 > i.posY > self.doc.posY - 1:
                    morts.append(i)

        for i in morts:
            t = TasFerraille(self, [i.posX, i.posY])
            self.tdf.append(t)
            self.daleks.remove(i)

        self.zap -= 1


class TasFerraille():
    def __init__(self, parent, pos):
        self.parent = parent
        self.posX, self.posY = pos


class Daleks():
    def __init__(self, parent, pos):
        self.parent = parent
        self.posX, self.posY = pos

    def deplacer(self):
        if self.posX < self.parent.doc.posX:
            self.posX += 1
        elif self.posX > self.parent.doc.posX:
            self.posX -= 1

        if self.posY < self.parent.doc.posY:
            self.posY += 1
        elif self.posY > self.parent.doc.posY:
            self.posY -= 1


class Docteur():
    def __init__(self, parent):
        self.parent = parent
        self.posX = random.randrange(self.parent.largeur)
        self.posY = random.randrange(self.parent.hauteur)

    def deplacer(self, modif):
        x, y = modif
        # NOTE eventuellement verifier les bordures
        for i in self.parent.tdf:
            if self.posX + x == i.posX and self.posY + y == i.posY:
                self.posX = self.posX
                self.posY = self.posY

        if self.posX + x == self.parent.largeur or self.posX + x < 0:
            self.posX = self.posX
        else:
            self.posX += x

        if self.posY + y == self.parent.hauteur or self.posY + y < 0:
            self.posY = self.posY
        else:
            self.posY += y

    def tp(self):
        possible = False
        while possible is False:
            possible = True
            self.posX = random.randrange(self.parent.largeur)
            self.posY = random.randrange(self.parent.hauteur)
            for i in self.parent.tdf:
                if self.posX == i.posX and self.posY == i.posY:
                    possible = False

            for i in self.parent.daleks:
                if i.posX + 2 > self.posX > i.posX - 2:
                    if i.posY + 2 > self.posY > i.posY - 2:
                        possible = False


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
                                 "9": [1, -1],
                                 "t": "t",
                                 "z": "z"
                                 }

    def afficher_menu_jeu(self):
        print("t pour teleporter")
        print("z pour zapper    nombre de zap: " + str(self.modele.zap))
        rep = input("Indiquez votre coup (clavier num.): ")
        bonnereponse = False
        while bonnereponse is False:
            if rep not in self.dico_deplacement.keys():
                rep = input("touche invalide veuillez renvoyer une touche: ")
            else:
                bonnereponse = True
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

        for i in self.modele.tdf:
            tableau[i.posY][i.posX] = "T"

        print("Niveau " + str(self.modele.nivo))
        for i in tableau:
            print(i)

    def affiche_GameOver(self):
        score = self.modele.score
        print("GameOver")
        print("Score :" + str(score))


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.afficher_jeu()
        self.jouer_partie()

    def jouer_partie(self):
        rep = self.vue.afficher_menu_jeu()
        reponse = self.modele.jouer_coup(rep)
        self.modele.dalek_move()
        self.modele.verif_collision()
        self.vue.affiche_tableau()
        if self.modele.gameover is False:
            if len(self.modele.daleks) == 0:
                self.modele.creer_nivo()
                self.vue.affiche_tableau()
            self.jouer_partie()
        else:
            self.vue.affiche_GameOver()

    def afficher_jeu(self):
        self.vue.affiche_tableau()


if __name__ == "__main__":
    controleur = Controleur()

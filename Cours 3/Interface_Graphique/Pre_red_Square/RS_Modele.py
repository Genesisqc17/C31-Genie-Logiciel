
import random
from helper import Helper as hp

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 1000
        self.pion = Pion(self, self.largeur/2, self.hauteur/2)
        self.blocs = []

    def changer_position(self, new_pos):
        self.pion.changer_position(new_pos)

    def creer_bloc(self):
        for i in range(100):
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            p = Bloc(self, x, y)
            self.blocs.append(p)

    def deplacer_blocs(self):
        for p in self.blocs:
            p.deplacer()


class Pion():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 30
        self.posX = x
        self.posY = y
        self.couleur = "red"

    def changer_position(self, pos_souris):
        self.posX, self.posY = pos_souris



class Bloc():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 30
        self.vitesse = random.randrange(3,9)
        self.posX = x
        self.posY = y
        self.couleur = "blue"
        self.cibleX = None
        self.cibleY = None
        self.angle = None

    def trouver_cible(self):
        self.cibleX = random.randrange(self.parent.largeur)
        self.cibleY = random.randrange(self.parent.hauteur)
        self.angle = hp.calcAngle(self.posX,self.posY,self.cibleX,self.cibleY)

    def deplacer(self):
        if self.cibleX:
            self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
            dist = hp.calcDistance(self.posX, self.posY, self.cibleX, self.cibleY)
            if dist <= self.vitesse:
                self.trouver_cible()
        else:
            self.trouver_cible()
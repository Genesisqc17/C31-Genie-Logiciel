# Library tkinter pour interface graphique
# Library a ajouter PIL = Pillow (photoshop en code)

# window = interface graphique qui affiche les donnees dans la memoire
# windows premier a afficher plusieurs window graphique

# EVENTLOOP (ou MainLoop) loop dans des registres pour voir si une action(entree clavier, souris, microphone,
# etc) est arriver

# __main__ est ce qui est passer a python.exe pour etre interpreter

# import tkinter dans __main__ au lieu que dans son propre namespace
import helper
from tkinter import *
import random
from helper import Helper as hp


# import tkinter dans son propre namespace
# import tkinter as tk


class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()  # va initialiser l'engin graphique et retourner une fenetre
        self.root.title("Jeu carre rouge")

        # gestionnaire de geometrie ds Tk:
        # pack ( pack sont contenu de gauche a droite ),
        # grid ( place en 2d [column,row] ),
        # place ( place en [x, y] ou en % )
        # un seul gestionnaire par widget ou frame( contenant des widgets ) container
        # .pack().forget() pour vider le pack sans le detruire

        mavar = Label(self.root, text="Bienvenue au cours de C31_intensif")  # creer un widget
        mavar.pack()

        mavar2 = Button(self.root, text="Generateur", command=self.creer_jeu)
        mavar2.pack()

        mavar3 = Button(self.root, text="Lancer animation", command=self.animer)
        mavar3.pack()

        self.canevas = Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="dark sea green")
        self.canevas.bind("<Button>", self.activer)
        self.canevas.pack()

    def animer(self):
        self.parent.animer()

    def activer(self, evt):
        mestags = self.canevas.gettags("current")
        if "pion" in mestags:
            self.canevas.bind("<Motion>", self.changer_position)
            self.canevas.bind("<ButtonRelease>", self.desactiver)

    def desactiver(self, evt):
        self.canevas.unbind("<Motion>")
        self.canevas.unbind("ButtonRelease")

    def changer_position(self, evt):
        self.parent.changer_position((evt.x, evt.y))

    def creer_jeu(self):
        self.parent.creer_bloc()

    def afficher_blocs(self):
        self.canevas.delete("all")
        for p in self.modele.blocs:
            self.canevas.create_rectangle(p.posX, p.posY, p.posX+p.taille, p.posY+p.taille, fill=p.couleur, tags=("bloc", p.posX, p.posY), outline="sea green")

        p = self.modele.pion
        self.canevas.create_rectangle(p.posX, p.posY, p.posX + p.taille, p.posY + p.taille, fill=p.couleur,
                                      tags=("pion", p.posX, p.posY), outline="sea green")


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 1000
        self.pion = Pion(self, self.largeur/2, self.hauteur/2)
        self.blocs = []

    def changer_position(self,new_pos):
        self.pion.changer_position((new_pos.x, new_pos.y))

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


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()  # par le loop de la fenetre

    def creer_bloc(self):
        self.modele.creer_bloc()
        self.vue.afficher_blocs()
        print("nb blocs", len(self.modele.blocs))

    def deplacer_blocs(self):
        self.modele.deplacer_blocs()
        self.vue.afficher_blocs()

    def animer(self):
        self.modele.deplacer_blocs()
        self.vue.afficher_blocs()
        self.vue.root.after(50, self.animer)

    def changer_position(self, new_pos):
        self.modele.changer_position(new_pos)


if __name__ == "__main__":
    c = Controleur()

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

        # gestionnaire de geometrie ds Tk:
        # pack ( pack sont contenu de gauche a droite ),
        # grid ( place en 2d [column,row] ),
        # place ( place en [x, y] ou en % )
        # un seul gestionnaire par widget ou frame( contenant des widgets ) container
        # .pack().forget() pour vider le pack sans le detruire

        mavar = Label(self.root, text="Bienvenue au cours de C31_intensif")  # creer un widget
        mavar.pack()

        mavar2 = Button(self.root, text="Cours graphique", command=self.creer_pion)
        mavar2.pack()

        mavar3 = Button(self.root, text="Animer", command=self.animer)
        mavar3.pack()

        self.canevas = Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="dark sea green")
        self.canevas.bind("<Button>", self.get_position)
        self.canevas.pack()

    def animer(self):
        self.parent.animer()

    def get_position(self, evt):
        chose = self.canevas.find_withtag("current") # tag current = objet sous la souris
        if chose:
            print(chose,"x: ",evt.x,"y: ",evt.y)

    def creer_pion(self):
        self.parent.creer_pion()

    def afficher_pions(self):
        self.canevas.delete("all")
        for p in self.modele.pions:
            self.canevas.create_rectangle(p.posX, p.posY, p.posX+p.taille, p.posY+p.taille, fill=p.couleur, tags=("pion", p.posX, p.posY), outline="sea green")


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1000
        self.hauteur = 1000
        self.pions = []

    def creer_pion(self):
        for i in range(100):
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            p = Pion(self, x, y)
            self.pions.append(p)

    def deplacer_pions(self):
        for p in self.pions:
            p.deplacer()


class Pion():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 30
        self.vitesse = random.randrange(3,9)
        self.posX = x
        self.posY = y
        self.couleur = "orangered2"
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

    def creer_pion(self):
        self.modele.creer_pion()
        self.vue.afficher_pions()
        print("nb pions", len(self.modele.pions))

    def deplacer_pions(self):
        self.modele.deplacer_pions()
        self.vue.afficher_pions()

    def animer(self):
        self.modele.deplacer_pions()
        self.vue.afficher_pions()
        self.vue.root.after(50, self.animer)


if __name__ == "__main__":
    c = Controleur()

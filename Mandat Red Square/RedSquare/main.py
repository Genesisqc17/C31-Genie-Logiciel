import random
from tkinter import *
from helper import Helper as hp


##
class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.offset_x = 0
        self.offset_y = 0
        self.current_carre = None
        self.canevas = Canvas(self.root, width=self.modele.largeur,
                              height=self.modele.hauteur,
                              bg="black")
        self.canevas.pack()
        self.canevas.bind("<Button-1>", self.start_drag)
        self.canevas.bind("<B1-Motion>", self.dragging)
        self.canevas.bind("<ButtonRelease-1>", self.end_drag)
        # bouton_start = Button(self.root, text="Commencer partie", command=self.creer_carre)
        # bouton_start.pack()

    def start_drag(self, event):

        items_with_tag = self.canevas.find_withtag("red-square")

        if items_with_tag:
            self.current_carre = items_with_tag[0]
        self.offset_x = event.x - self.canevas.coords(self.current_carre)[0]
        # difference entre le click (event) et la bordure du red square
        self.offset_y = event.y - self.canevas.coords(self.current_carre)[1]
        print(self.offset_x, self.offset_y)

    def dragging(self, event):

        # bouger carre pour suivre curseur
        new_x, new_y = event.x - self.offset_x, event.y - self.offset_y
        # new_x,y = difference entre la position du curseur et le top-left du red square
        # pour donner la position exacte x,y du carre
        #
        print(new_x, new_y)
        self.canevas.coords(self.current_carre, new_x, new_y, new_x + self.modele.carres[0].taille,
                            new_y + self.modele.carres[0].taille)

    def end_drag(self, event):
        self.current_carre = None  # Clear carre

    def creer_carre(self):
        self.parent.creer_carre()  # demande cette fonction au controleur

    def afficher_carre(self):
        for i in self.modele.carres:
            self.canevas.create_rectangle(i.posX, i.posY,
                                          i.posX+i.taille,
                                          i.posY+i.taille, fill="red",
                                          outline="white",
                                          tags=("red-square",))


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 450
        self.hauteur = 450
        self.carres = []

    def creer_carre(self):
        x = 205
        y = 205
        car = Carre(self, x, y)
        self.carres.append(car)

class Carre():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.taille = 40
        self.posX = x
        self.posY = y
        self.cibleX= None
        self.cibleY = None
        self.angle = None
        self.vitesse =5



class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.creer_carre()
        self.vue.root.mainloop()

    def creer_carre(self):
        self.modele.creer_carre()
        self.vue.afficher_carre()
        print(len(self.modele.carres))


if (__name__ == "__main__"):
    c = Controleur()
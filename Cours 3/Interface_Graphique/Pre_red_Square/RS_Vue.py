from tkinter import *

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

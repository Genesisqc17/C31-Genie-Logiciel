

# python creer un objet mm si il ne contient rien
# __init__(self) ajoute des attributs a l'interieur de l'objet deja cree
class Vue():
    def __init__(self): # function utiliser a la creation de l'objet sur l'objet
        self.largeur = 10
        self.hauteur = 8

    def affiche_tableau(self):
        tableau = []
        for i in range(self.hauteur):
            ligne = []
            for j in range(self.largeur):
                ligne.append("*")
            tableau.append(ligne)
        #print(tableau)

        for i in tableau:
            print(i)



lavue = Vue()

lavue.affiche_tableau()
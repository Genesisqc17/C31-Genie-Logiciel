import RS_Modele as mod
import RS_Vue as vue

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
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
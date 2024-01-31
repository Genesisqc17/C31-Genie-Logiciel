# Note de cours Genie Logiciel


Client First


## Travail en equipe


Faire fi de nos preferences personnelles
++Communications

ChatGpt and all Ai should be a tool we're used too. It's use will be inevitable in the future.

**Informed yourself in your field of work**
*Yoshua Bengio*


## TimeBoxing


Work on a projet in a set time interval


## Projet


### 0- Mandat 
ecrit pour avoir preuvent et etre sur de ce que veut le client

### 1- Analyse textuelle
lire le mandat pour le comprendre

Developper une grille en 2d des termes importants du mandat
                ________________________________
                |Nom   |  Verbe   |    Adjectif|
    explicite   |______|__________|____________| exemple: Envoyer un courriel
    implicite   |______|__________|____________| exemple: Addresse courriel
supplementaire  |______|__________|____________| exemple: login Date and hour for a login tool

### 2- Identification des cas d'usages
Comment le client va utiliser le produit

liste de petites phrases courtes
Exemple:
- Faire rapport semaine
- Inscrire Facture
- Entrer dans Inventaire

### 3- Constitution des scenarios d'utilisation
Sequence d'etapes les unes apres les autres pour que notre cas d'usage soit possible

**En informatique, les mots(expressions) viennent du language ordinaire** 
?Heuristique? contrepartie de Algorithme (processus qui garantie une fin)

Pour tous les cas d'usages
Temporel (Chaque Etapes ce suis)
*Echange entre Humain et Machine*
            ______________________________
            |    Humain   |   Machine    |
            |_____________|______________|  1.Humain: choisir menu rapport
            |_____________|______________|  2.Machine: Afficher le rapport
            |_____________|______________|  3.Humain: Inscrire date
            |_____________|______________|  4.Humain: cliquer sur Entrer
                                            5.Machine: Lire la date
                                            6.Machine: Faire une requete SQL
                                            7.Machine: Utilise les donnees pour generer graphique
                                            8.Machine: Afficher graphique
                                            9.Humain: Choisir sauvegarde image

#### 3.b- Maquette d'interface
- Organiser les pages d'écran
- Fonctionnalité plus que look


### 4- Classe
Modele CRC *from Xtreme Programming (XP)*
        ______________________________________________
        |Classe:             Nom       |Collaborateurs| Dans classe Rajouter des responsables(Personne responsable de cette classe)
        |______________________________|______________|
        |Responcabilitées:   Jobs      |______________| Methodes (et arguments)
        |______________________________|______________|

        Classe      SQLParser               
        Responsable : John                  

        Responcabilitees: Methodes(args)


### 5- Modélisation de données (Base de données)
Base de donnees relationnel (tables SQL)

### 6- Planification Globale
Division de la charge de travail en SPRINTs(TimeBoxing)

    Planif          1               2               3               4           Remise Final
                ^___________^^____________^^^_____________^^^^____________^^^^^

SPRINT = 2 a 4 sem
Livrables Partiels

Etapes 1 a 5 (Planif) = entre 20 et 40% du temps allouer au projet

**80% de la programmation n'atteind pas le client**
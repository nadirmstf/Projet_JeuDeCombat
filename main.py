from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())

MENU = ["Jouer","meilleurs scores", "quitter"]

#menu
    #tant que vrais
        #recuperer un choix valide parmis options(MENU)
        #lancer le choix




#afficher des proposition(MENU)
    #pour i, proposition dans enumerate(MENU, i)
    #afficher i " - " proposition
    #i = i + 1
    #retourner i


#demander un choix valide(options)
    #tant que vrai
        # afficher les options numeroter
        # choix = input("entrez votre choix")
        # si choix valide(taille des options)
        #   retourner le choix
        # afficher message d'erreur


#verifier si choix est valide
    #si choix n'est pas isdigit()
        #retourner faux

    #convertir en entier
    #si choix n'est pas compris entre 1 inclus et le nombre de choix inclus
        #retourner faux

    #retourner vrais


#lancer le choix
    #si choix == 1
        #jeu
    #si choix == 2
        #meilleurs scores
    #si choix == 3
        #retourner faux





#jeu
    #démarrage du jeu
    #lancer le combat
    #resultat


#démarrage du jeu
    #demander un pseudo
    #créer équipe heros
    #créer équipe monstres
    #afficher équipe heros vs équipe monstres
    #définir le premier qui attaque


#créer équipe heros
    #demander un nom d'équipe
    #demander un nombre de combattant (max 5)
    #tant que i n'est pas égale nombre de combattant
        #recuperer un choix valide parmis options(Personnages)


#créer équipe monstres
    #choisir un nom random
    #tant que i n'est pas égale nombre de combattant
        #choisir une équipe random


#choisir un nom random
    #i = chiffre random compris entre 1 et le nombre totale de nom possible
    #nom = liste de nom [i]

#choisir une équipe random
    #i = chiffre random compris entre 1 et le nombre totale de monstre dans la liste monstres
    #nom = liste de monstres [i]
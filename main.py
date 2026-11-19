from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())
nom_random_monstres =[]

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
    #combat
    #resultat


#démarrage du jeu
    #demander un pseudo
    #créer équipe heros
    #créer équipe monstres
    #afficher équipe heros vs équipe monstres
    #définir le premier qui attaque
    #retourner la liste hero, la liste monstre, le nom des équipe et i



#créer équipe heros
    #hero = []
    #demander un nom d'équipe
    #demander un nombre de combattant valide (max 5)
    #tant que i n'est pas égale nombre de combattant choisis
        #recuperer un choix valide parmis options(Personnages)
        #ajouter le personnage a la liste hero
    #retourner la liste hero et nom d'équipe

#demander un nombre de combattant valide (max 5)
    #input("combien de combattant voulez vous ? maximum 5")
    #verifier si choix est valide
    #retourner le nombre de combattant choisis

#recuperer un choix valide parmis options(Personnages)
    #input(quel combattant voulez vous ?)
    #verifier si choix est valide
    #retourner le choix



#créer équipe monstres
    #équipe_monstres = []
    #choisir un nom random
    #tant que i n'est pas égale a la longueure de la liste hero
        #choisir un monstre random
        #ajouter le monstre a la liste équipe_monstres
    #retourner équipe monstres et nom random


#choisir un nom random
    #i = chiffre random compris entre 1 et le nombre totale de nom possible
    #nom = liste de nom [i]
    #retourner nom


#choisir un monstre random
    #i = chiffre random compris entre 1 et le nombre totale de monstre dans la liste monstres
    #monstre = liste de monstres [i]
    #retourner monstre


#définir le premier qui attaque
    #i = choisir un chiffre random entre 1 et 2
    #si i == 1
        #afficher joueur attaque en premier
        #retourner i
    #afficher monstres attaquent en premier
    #retourner i











#combat
    #tant que vrais
        #afficher a qui le tour
        #choisir l'attaque
        #verifier si personnage mort
        #verifier si équipe morte
        #resultat de l'attaque
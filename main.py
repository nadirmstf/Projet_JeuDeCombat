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
    #retourner la liste hero, la liste monstre et le nom des équipe 



#créer équipe heros
    #equipe_heros = []
    #demander un nom d'équipe
    #demander un nombre de combattant valide (max 5)
    #tant que i n'est pas égale nombre de combattant choisis
        #heros_disponibles = determiner disponibilité (personnage, personnages, equipe)
        #recuperer un choix valide parmis options(heros_disponibles)
        #ajouter le personnage a la liste hero
    #retourner la liste hero et nom d'équipe



#determiner disponibilité (elements, liste_A, liste_B)
    #disponible
    #pour elements dans liste_A
        #si elements n'est pas dans liste_B
            #ajouter elements dans disponible
            #retourner disponible



#demander un nombre de combattant valide (max 5)
    #input("combien de combattant voulez vous ? maximum 5")
    #verifier si choix est valide
    #retourner le nombre de combattant choisis

#recuperer un choix valide parmis options(Personnages)
    #afficher des proposition(hero_disponibles)
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
        #mort = []
        #si i == 1 alors
            #afficher c'est au tour des heros
            #equipe_hero_en_jeux = determiner disponibilité (hero, equipe_hero, mort)
            #monstres_en_jeux = determiner disponibilité (monstre, equipe_monstres, mort)
            #choisir sur qui lancer l'attaque
            #choisir quel hero attaque
            #verifier si personnage mort
            #verifier si équipe morte
            #resultat de l'attaque

        #si i == 2 alors
            #afficher c'est au tour des monstres




#choisir sur qui lancer l'attaque
    #afficher des proposition(monstres_en_jeux)
    #monstre_attaqué = demander un choix valide(options)


#choisir quel hero attaque
    #afficher des proposition(equipe_hero_en_jeux)
    #hero_qui_attaque = demander un choix valide(options)
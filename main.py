from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())
nom_random_monstres =[]

MENU = ["Jouer","meilleurs scores", "quitter"]

derniers_scores = []

def menu():
    while True:
        choix = demander_choix_valide(MENU)
        lancer_le_choix(choix)




def afficher_des_propositions(propositions):
    for i, proposition in enumerate(propositions):
        print(i, " - ", proposition)
        i =+ 1
        return i


def demander_choix_valide(option):
    while True :
        afficher_des_propositions(option)
        choix = input("entrez votre choix : ")
        verifier_si_choix_valide(choix, option)
        print("erreur, réessayez !")


def verifier_si_choix_valide(choix, liste_choix):
    if not choix.isdigit():
        return False

    choix = int(choix)
    if not 1 <= choix < len(liste_choix):
        return False

    return True


def lancer_le_choix(choix):
    if choix == 1 :
        #jeu
        print("vous avez choisis 1 !")
    elif choix == 2 :
        #meilleurs scores
        print("vous avez choisis 2 !")
    elif choix == 3 :
        #retourner faux
        print("vous avez choisis 3 !")





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
    #retourner la liste hero, la liste monstre, le nom des équipe et equipe_commence



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


#choix random (list)
    #i = chiffre random compris entre 1 et le nombre totale de nom possible
    #element_choisis = liste de nom [i]
    #retourner nom



#définir le premier qui attaque
    #i = choix random entre vrais et faux
    #si i == vrais
        #equipe_commence == vrais
        #afficher joueur attaque en premier
        #retourner equipe_commence

    #equipe_commence == faux    
    #afficher monstres attaquent en premier
    #retourner equipe_commence























#combat
    #manche = 1
    #tant que statut_equipe_hero == vrais
        #mort = []
        #si equipe_commence == vrais :
            #tour heros
            #tour monstres

        #sinon:
            #tour monstres
            #tour heros

    #retourner manche




#tour heros
        #equipe_hero_en_jeux = determiner disponibilité ( equipe_hero, mort)
        #monstres_en_jeux = determiner disponibilité ( equipe_monstres, mort)
        #verifier mort equipe monstres
        #afficher "c'est au tour des heros"
        #attaque


#tour monstres
        #equipe_hero_en_jeux = determiner disponibilité ( equipe_hero, mort)
        #monstres_en_jeux = determiner disponibilité ( equipe_monstres, mort)
        #verifier mort equipe monstres
        #afficher c'est au tour des monstres
        #attaque random
        #equipe_hero_en_jeux = determiner disponibilité ( equipe_hero, mort)
        #verification mort equipe_hero


#attaque random
    #choix random sur qui lancer l'attaque
    #choix random de qui lance l'attaque
    #retirer des pv (hero_qui_attaque, monstre_attaqué)
    #resultat de l'attaque


#attaque
    #choisir sur qui lancer l'attaque
    #choisir quel hero attaque
    #retirer des pv (hero_qui_attaque, monstre_attaqué)
    #resultat de l'attaque

#verification mort equipe_hero
    #si equipe_hero_en_jeux == []
        #afficher vous etes mort
        #statut_equipe_hero == faux
        #retourner statut_equipe_hero



#verifier mort equipe monstre
    #si monstres_en_jeux == []
        #manche  = manche + 1
        #vous avez gagner la premiere manche, voici la prochaine equipe a affronter
        #créer équipe monstres
        #afficher nouvelle equipe monstres


#choisir sur qui lancer l'attaque
    #afficher des proposition(monstres_en_jeux)
    #monstre_attaqué = demander un choix valide(options)
    #retourner monstre_attaqué


#choisir quel hero attaque
    #afficher des proposition(equipe_hero_en_jeux)
    #hero_qui_attaque = demander un choix valide(options)
    #retourner hero_qui_attaque



#retirer des pv (attaquant, cible)
    #degats = attaque de l'attaquant
    #pv de la cible = pv de la cible - degats

    #si pv de la cible <= 0
        #pv de la cible = 0
        #afficher ce personnage est mort
        #ajouter la cible a la liste mort

    #afficher nom de la cible et pv restants























#resultat
    #afficher message d'encouragement, et nombre de manche reussite
    #ajouter à derniers_scores










menu()
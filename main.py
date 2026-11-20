from pymongo import MongoClient
import random

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["Data"]

personnages = db["personnages"].find_one()["personnages"] 
monstres = db["Monstres"].find_one()["monstres"]      
nom_personnages = [perso["nom"] for perso in personnages]
nom_random_monstres = db["NomsEquipesMonstres"].find_one()["noms_equipes_monstres"]
MENU = ["Jouer","meilleurs scores", "quitter"]

derniers_scores = []

def menu():
    while True:
        choix = demander_choix_valide(MENU)
        lancer_le_choix(choix)




def afficher_des_propositions(propositions):
    for i, proposition in enumerate(propositions, start = 1):
        print(i, " - ", proposition)


def demander_choix_valide(option):
    while True :
        afficher_des_propositions(option)
        choix = input("entrez votre choix : ")
        if verifier_si_choix_valide(choix, option) :
            return int(choix)
        print("erreur, réessayez !")


def verifier_si_choix_valide(choix, liste_choix):
    if not choix.isdigit():
        return False

    choix = int(choix)
    if not 1 <= choix <= len(liste_choix):
        return False

    return True


def lancer_le_choix(choix):
    if choix == 1 :
        jeu()
        print("vous avez choisis de jouer !")
    elif choix == 2 :
        #meilleurs scores
        print("vous avez choisis 2 !")
    elif choix == 3 :
        #retourner faux
        print("vous avez choisis 3 !")





def jeu():
    equipe_heros, equipe_monstres, nom_equipe_heros, nom_equipe_monstres, equipe_commence = demarrer_jeu()
    #combat
    #resultat


def demarrer_jeu():
    pseudo = input("Entrez votre pseudo : ")
    equipe_heros, nom_equipe_heros = creer_equipe_heros()
    equipe_monstres, nom_equipe_monstres = creer_equipe_monstres(equipe_heros)

    print(nom_equipe_heros, "VS", nom_equipe_monstres)
    print(equipe_heros)
    print(equipe_monstres)

    equipe_commence = definir_premier_qui_attaque()
    return equipe_heros, equipe_monstres, nom_equipe_heros, nom_equipe_monstres, equipe_commence


def creer_equipe_heros():
    equipe_heros = []
    nom_equipe = input("Entrez le nom de votre équipe : ")
    nombre_combattants = demander_nombre_combattant_valide(5)

    for i in range(nombre_combattants):
        heros_disponibles = determiner_disponibilite(personnages, equipe_heros)
        noms = [heros["nom"] for heros in heros_disponibles]
        choix = recuperer_choix_valide_parmis_options(noms, "Quel combattant voulez-vous ? ")
        equipe_heros.append(heros_disponibles[choix - 1])

    return equipe_heros, nom_equipe


def determiner_disponibilite(liste_A, liste_B):
    disponible = []

    for elements in liste_A:
        if elements not in liste_B:
            disponible.append(elements)

    return disponible



def demander_nombre_combattant_valide(maximum):
    while True:
        choix = input("Combien de combattants voulez-vous ? Maximum 5 : ")

        if verifier_si_choix_valide(choix, list(range(1, maximum + 1))):
            return int(choix)

        print("Erreur, réessayez !")


def recuperer_choix_valide_parmis_options(options, question="Quel est votre choix ? "):
    afficher_des_propositions(options)

    choix = input(question)

    while not verifier_si_choix_valide(choix, options):
        print("Erreur, réessayez !")
        afficher_des_propositions(options)
        choix = input(question)

    return int(choix)


def creer_equipe_monstres(equipe_heros):
    equipe_monstres = []

    nom_equipe = choix_random(nom_random_monstres)

    while len(equipe_monstres) < len(equipe_heros):
        monstre = choix_random(monstres)

        if monstre not in equipe_monstres:
            equipe_monstres.append(monstre)

    return equipe_monstres, nom_equipe


def choix_random(liste):

    i = random.randint(0, len(liste) - 1)

    element_choisis = liste[i]

    return element_choisis



def definir_premier_qui_attaque():

    i = random.choice([True, False])

    if i == True:
        equipe_commence = True
        print("Les joueurs attaquent en premier !")
        return equipe_commence

    equipe_commence = False
    print("Les monstres attaquent en premier !")

    return equipe_commence























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
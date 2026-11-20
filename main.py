from pymongo import MongoClient
import random

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["Data"]

personnages = db["personnages"].find_one()["personnages"] 
monstres = db["Monstres"].find_one()["monstres"]      
nom_personnages = [perso["nom"] for perso in personnages]
nom_random_monstres = db["nom_monstres"].find_one()["noms_equipes_monstres"]
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
    if choix == 1:
        jeu()
    elif choix == 2:
        print("vous avez choisis 2 !")
    elif choix == 3:
        return False
    return True





def jeu():
    pseudo, equipe_heros, equipe_monstres, nom_equipe_heros, nom_equipe_monstres, equipe_commence = demarrer_jeu()
    manche = combat(equipe_heros, equipe_monstres, equipe_commence)
    resultat(pseudo, nom_equipe_heros, manche)


def demarrer_jeu():
    pseudo = input("Entrez votre pseudo : ")
    equipe_heros, nom_equipe_heros = creer_equipe_heros()
    equipe_monstres, nom_equipe_monstres = creer_equipe_monstres(equipe_heros)

    print(nom_equipe_heros, "VS", nom_equipe_monstres)

    equipe_commence = definir_premier_qui_attaque()
    return pseudo, equipe_heros, equipe_monstres, nom_equipe_heros, nom_equipe_monstres, equipe_commence


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















def combat(equipe_heros, equipe_monstres, equipe_commence):
    manche = 1
    statut_equipe_hero = True
    mort = []

    while statut_equipe_hero == True:
        if equipe_commence == True:
            tour_heros(equipe_heros, equipe_monstres, mort)
            tour_monstres(equipe_monstres, equipe_heros, mort)
        elif equipe_commence == False:
            tour_monstres(equipe_monstres, equipe_heros, mort)
            tour_heros(equipe_heros, equipe_monstres, mort)

        statut_equipe_hero = verification_mort_equipe_hero(equipe_heros, mort)

        if statut_equipe_hero == True and verifier_mort_equipe_monstre(equipe_monstres, mort):
            manche = manche + 1
            print("\nVous avez gagné la manche", manche - 1,"! Voici la prochaine équipe à affronter.")
            equipe_monstres, nom_equipe_monstres = creer_equipe_monstres(equipe_heros)
            print("Nouvelle équipe de monstres :", nom_equipe_monstres)

    return manche



def tour_heros(equipe_heros, equipe_monstres, mort):
    if verifier_mort_equipe_monstre(equipe_monstres, mort):
        return

    equipe_hero_en_jeux = determiner_disponibilite(equipe_heros, mort)
    monstres_en_jeux = determiner_disponibilite(equipe_monstres, mort)

    print("\nC'est au tour des héros")
    attaque(equipe_hero_en_jeux, monstres_en_jeux, mort)


def tour_monstres(equipe_monstres, equipe_heros, mort):
    if verification_mort_equipe_hero(equipe_heros, mort) == False or verifier_mort_equipe_monstre(equipe_monstres, mort):
        return

    equipe_hero_en_jeux = determiner_disponibilite(equipe_heros, mort)
    monstres_en_jeux = determiner_disponibilite(equipe_monstres, mort)

    print("\nC'est au tour des monstres")
    attaque_random(monstres_en_jeux, equipe_hero_en_jeux, mort)


def attaque_random(monstres_en_jeux, equipe_hero_en_jeux, mort):
    monstre = choix_random(monstres_en_jeux)
    hero = choix_random(equipe_hero_en_jeux)

    retirer_pv(monstre, hero, mort)


def attaque(equipe_hero_en_jeux, monstres_en_jeux, mort):
    hero = choisir_quel_hero_attaque(equipe_hero_en_jeux)
    monstre_attaque = choisir_sur_qui_attaquer(monstres_en_jeux)

    retirer_pv(hero, monstre_attaque, mort)


def verification_mort_equipe_hero(equipe_heros, mort):
    equipe_hero_en_jeux = determiner_disponibilite(equipe_heros, mort)
    statut_equipe_hero = True

    if equipe_hero_en_jeux == []:
        print("Vous êtes mort...")
        statut_equipe_hero = False

    return statut_equipe_hero



def verifier_mort_equipe_monstre(equipe_monstres, mort):
    monstres_en_jeux = determiner_disponibilite(equipe_monstres, mort)

    if monstres_en_jeux == []:
        return True

    return False


def choisir_sur_qui_attaquer(monstres_en_jeux):
    noms = [monstre["nom"] for monstre in monstres_en_jeux]
    choix = recuperer_choix_valide_parmis_options(noms, "Quelle cible ? ")
    return monstres_en_jeux[choix - 1]


def choisir_quel_hero_attaque(equipe_hero_en_jeux):
    noms = [hero["nom"] for hero in equipe_hero_en_jeux]
    choix = recuperer_choix_valide_parmis_options(noms, "Quel héros attaque ? ")
    return equipe_hero_en_jeux[choix - 1]



def retirer_pv(attaquant, cible, mort):
    degats = attaquant["pouvoir"]["degats"]
    cible["pv"] = cible["pv"] - degats

    print(attaquant["nom"], "attaque", cible["nom"], "et inflige", degats, "dégâts")

    if cible["pv"] <= 0:
        cible["pv"] = 0
        print(cible["nom"], "est mort !")
        mort.append(cible)

    print(cible["nom"], "a maintenant", cible["pv"], "PV")























def resultat(pseudo, nom_equipe_heros, manche):
    manches_reussies = manche - 1

    print("Bravo", pseudo, "! L'équipe", nom_equipe_heros, "a réussi", manches_reussies, "manche(s).")

    derniers_scores.append([pseudo, manches_reussies])






menu()
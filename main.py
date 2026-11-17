from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())



#menu
    #afficher des proposition
    #demander un choix
    #verifier si le choix est valide
    #lancer le choix
 
#jeu
    #démarrage du jeu
    #lancer le combat


#démarrage du jeu
    #demander un pseudo
    #demander un nom d'équipe
    #afficher les heros
    #demander de choisir 3 heros
    #les ajoutés a la liste team_heros
    #afficher l'equipe des heros
    #choisir les monstres de maniere random
    #les ajoutés a la liste team_monstres
    #afficher le nom de l'équipe et contre qu'elle équipe de monstres elle va se battre
    #definir qui commence en premier de maniere random
    #afficher qui commence en premier


#lancer le combat
    #tant que vrai
        #afficher les personnage disponible
        #si c'est le tour des monstres
            #les monstres attaque en random
        #si c'est le tour des hero
            #les heros attaquent


#les heros attanquent
    #demander quelle hero attaque
    #si hero mort
        #message d'erreur
    #si hero vivant
        #afficher les possibilité d'attaque
        #verifier si le choix est valide
        #lancer le choix
        #enlever des pv en fonction de l'attaque choisi

        #pour hero dans la liste team_heros
            #si statut = "mort"
                #afficher message de défaites
                #retourner faux
            #si statut = "vivant"
                #retourner vrais
        
        #pour monstre dans l'équipe team_monstres
            #si statut = "mort"
                #afficher message de victoire
                #retourner faux
            #si statut = "vivant"
                #retourner vrais

        #si pv du hero attaqué = 0
            #statut mort
            #afficher se hero est mort

        #si pv du monstre attaqué = 0
            #statut mort
            #afficher se monstre est mort

        #sinon
            #afficher se personnage a perdu x pv


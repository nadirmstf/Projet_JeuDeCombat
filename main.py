from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())


#afficher des propostion(liste de proposition):
    





#démarrage du jeu
    #demander un pseudo
    #demander un nom d'équipe
    #afficher les heros
    #demander de choisir 3 heros
    #afficher l'equipe des heros
    #choisir les monstres de maniere random
    #afficher le nom de l'équipe et contre qu'elle équipe de monstres elle va se battre
    #definir qui commence en premier de maniere random
    #afficher qui commence en premier



#menu
    #afficher des proposition
    #demander un choix
    #verifier si le choix est bon
    #lancer le choix
#jeu
    #démarrage du jeu
    #lancer le combat
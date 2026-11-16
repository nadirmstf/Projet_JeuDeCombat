from pymongo import MongoClient

#initialisation de la bdd
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]

personnages = list(db["personnages"].find())
monstres = list(db["monstres"].find())


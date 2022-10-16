from sys import path
import json

from Serveur.DAO.dao import Dao
from Utils import utils

path.append('./DAO')
# from Serveur.DAO.dao import Dao


path.append('../Utils')
# import Utils.utils as utils



# class Controleur_Serveur(Controleur):
class Controleur_Serveur:
    def __init__(self):
        self.fonctions = {
            utils.IDENTIFIER_USAGER: self.identifier_usager,
            utils.CREER_COMPTE_VILLE: self.creer_compte_ville
        }

    # Le nom de la fonction voulue est envoyée
    # par le controleur_client et reçu par le
    # controleur_serveur dans le request.form
    # la réponse de la BD est JSON-ifiée
    def reponse(self, request_form):
        fonction_str = request_form[utils.FONCTION]
        fonction = self.fonctions[fonction_str]
        infos = fonction(request_form)
        return json.dumps(infos)

    # instance de sqlite3 doit être utilisée dans le même
    # thread que celui de sa création
    def identifier_usager(self, form):
        nom = form[utils.NOM]
        mdp = form[utils.MDP]
        return Dao().identifier_usager(nom, mdp)

    def creer_compte_ville(self, form):
        return Dao().insert_compagnie(form[utils.NOM_VILLE], form[utils.PAYS], form[utils.PROVINCE], form[utils.REGION])

    def creer_usager(self, form):
        prenom = form[utils.NOM]
        identifiant = form[utils.IDENTIFIANT]
        mdp = form[utils.MDP]
        titre = form[utils.TITRE]
        genre = form[utils.GENRE]
        id_compagnie = form[utils.ID_COMPAGNIE]
        permission = form[utils.PERMISSION]

    def creer_compte_admin(self, nom_admin, mdp_admin):
        # permission ultime
        pass

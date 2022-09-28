import json
from dao import Dao

from sys import path
path.append('../Utils')
import Utils.utils as utils


# class Controleur_Serveur(Controleur):
class Controleur_Serveur:
    def __init__(self):
        self.fonctions = {
            utils.IDENTIFIER_USAGER:self.identifier_usager
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
        
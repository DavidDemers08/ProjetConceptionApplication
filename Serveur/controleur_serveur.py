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
        nom = form[utils.NOM_USAGER]
        mdp = form[utils.MDP]
        return Dao().identifier_usager(nom, mdp)

    def creer_compte_ville(self, form) -> str:
        try:
            Dao().insert_compagnie(form[utils.NOM_VILLE], form[utils.PAYS], form[utils.PROVINCE], form[utils.REGION])
            id_compagnie = Dao().select_id_of_compagnie(form[utils.NOM_VILLE])


            self.creer_compte_admin(nom=form[utils.NOM],prenom= form[utils.PRENOM],id_compagnie= id_compagnie,genre=form[utils.GENRE],mdp_admin=form[utils.MDP],identifiant=form[utils.NOM_USAGER])
            return f"la ville suivante a été ajoutée : {form[utils.NOM_VILLE]} ainsi que l'administrateur suivant : " \
                   f"{form[utils.NOM_USAGER]} "
        except:
            return "Impossible d'ajouter votre compagnie"

    def creer_usager(self, form):
        prenom = form[utils.PRENOM]
        identifiant = form[utils.IDENTIFIANT]
        mdp = form[utils.MDP]
        titre = form[utils.TITRE]
        genre = form[utils.GENRE]
        id_compagnie = form[utils.ID_COMPAGNIE]
        permission = form[utils.PERMISSION]

    def creer_compte_admin(self, identifiant: str, mdp_admin: str, id_compagnie: int,genre: str ,nom: str,prenom:str) -> str:
        try:
            Dao().insert_membre(prenom=prenom,nom=nom,identifiant=identifiant,mdp=mdp_admin,id_compagnie=id_compagnie,titre="admin",permission="1",genre=genre)

        except:
            print(Exception)





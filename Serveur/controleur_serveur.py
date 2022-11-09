from sys import path
from Serveur.DAO.dao import Dao
from Utils import utils
import json


#path.append('./DAO')
# from Serveur.DAO.dao import Dao


#spath.append('../Utils')


# import Utils.utils as utils


# class Controleur_Serveur(Controleur):
class Controleur_Serveur:
    def __init__(self):

        self.fonctions = {
            utils.IDENTIFIER_USAGER: self.identifier_usager,
            utils.CREER_COMPTE_VILLE: self.creer_compte_ville,
            utils.AFFICHER_MEMBRES: self.afficher_membres,
            utils.AFFICHER_COMPAGNIES: self.afficher_compagnies,
            utils.CREER_ACCES: self.creer_acces,
            utils.GET_MODULE: self.get_module,
            utils.VOIR_INFOS_USAGER: self.voir_infos_usager
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

    def voir_infos_usager(self, form):
        compagnies = Dao().select_all_compagnie_de_membre(form[utils.NOM_USAGER])
        employes = []
        for compagnie in compagnies:
            nom_compagnie = Dao().select_nom_compagnie(compagnie[1])
            employes.append(Dao().select_all_membres_de_compagnie(nom_compagnie))
        return employes

    def creer_compte_ville(self, form) -> str:
        try:
            Dao().insert_compagnie(form[utils.NOM_VILLE], form[utils.PAYS], form[utils.PROVINCE], form[utils.REGION])
            id_compagnie = Dao().select_id_of_compagnie(form[utils.NOM_VILLE])

            return self.creer_compte_admin(nom=form[utils.NOM], prenom=form[utils.PRENOM], id_compagnie=id_compagnie,
                                           genre=form[utils.GENRE], mdp_admin=form[utils.MDP],
                                           identifiant=form[utils.NOM_USAGER])
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

    def creer_compte_admin(self, identifiant: str, mdp_admin: str, id_compagnie: int, genre: str, nom: str,
                           prenom: str):
        try:
            return Dao().insert_membre(prenom=prenom, nom=nom, identifiant=identifiant, mdp=mdp_admin,
                                       id_compagnie=id_compagnie, titre="admin", permission=1, genre=genre,
                                       nom_access="Super_Admin")

        except:
            return Exception

    def voir_membre(self, form):
        membre = []
        for rangee in Dao().select_all_membres():
            membre.append(rangee)
            print(rangee)
        return membre



    def voir_compagnie(self, form):
        compagnie = []
        for rangee in Dao().select_all_compagnies():
            compagnie.append(rangee)
        return compagnie

    def voir_membre_all_compagnie(self, form):
        membre = []
        for rangee in Dao().select_membres_all_compagnie():
            membre.append(rangee)
        return membre

    def afficher_membres(self, form):
        return self.voir_membre(form)

    def afficher_compagnies(self, form):
        return self.voir_compagnie(form)

    def creer_acces(self, form):
        return Dao().insert_acces(form[utils.NOM_ACCES])

    def liaison_acces_module(self, form):
        pass

    def get_module(self, form):
        module = ["stuff"]
        # for range in Dao.select_all_modules_of_compagnie(1):
        #    module.append(range)
        return module


if __name__ == "__main__":
    Dao().creer_bd()
    Dao().ajouter_acces_super_admin()
    Dao().ajouter_modules_initiaux()
    Dao().ajouter_lien_acces_module_super_admin()

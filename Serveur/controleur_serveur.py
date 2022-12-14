from sys import path

import Utils.utils
from Serveur.DAO.dao import Dao
from Utils import utils
import json


# path.append('./DAO')
# from Serveur.DAO.dao import Dao


# spath.append('../Utils')


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
            utils.VOIR_COMPAGNIE_ID_UTILISATEUR: self.voir_compagnie_id_utilisateur,
            utils.CREER_USAGER: self.creer_usager,
            utils.VOIR_INFOS_USAGER: self.voir_infos_usager,
            utils.CHERCHER_COMPAGNIE: self.chercher_compagnie,
            utils.GET_ACCESS: self.get_access,
            utils.GET_USERNAME_ID: self.get_username_id,
            utils.GET_MODULE_ID_BY_USER_ID:self.get_module_id_by_user_id,
            utils.ADD_TEST_DATA: self.add_test_data,
            utils.GET_MODULE_WITH_ACCESS_ID: self.get_module_with_access_id,
            utils.GET_MODULE_ID_BY_COMPANY_ID: self.get_module_id_by_company_id,
            utils.NOM_COMPAGNIE: self.nom_compagnie,
            utils.DELETE_MEMBRE: self.delete_membre,

            utils.ID_COMPAGNIE: self.id_compagnie,
            utils.CHERCHER_EMPLOYES_COMPAGNIE: self.chercher_employes_compagnie,

        }

    # Le nom de la fonction voulue est envoyée
    # par le controleur_client et reçu par le
    # controleur_serveur dans le request.form
    # la réponse de la BD est JSON-ifiée

    def chercher_employes_compagnie(self, form):
        id_comp = Dao().select_all_compagnie_de_membre(form[utils.ID_MEMBRE])[0][1]
        users_id = Dao().select_all_id_membres_de_compagnie(id_compagnie=id_comp)
        users = []
        for id in users_id:
             infos = Dao().select_infos_membres_by_id(id[0])
             users.append(infos[0])
        return users

    def delete_membre(self, form):
        Dao().delete_membre(form[utils.IDENTIFIANT])




    def reponse(self, request_form):
        fonction_str = request_form[utils.FONCTION]
        fonction = self.fonctions[fonction_str]
        infos = fonction(request_form)
        return json.dumps(infos)

    def chercher_compagnie(self, form):
        nom_ville = form[utils.NOM_VILLE]
        return Dao().select_id_of_compagnie(nom_ville)

    # instance de sqlite3 doit être utilisée dans le même
    # thread que celui de sa création
    def identifier_usager(self, form):
        nom = form[utils.NOM_USAGER]
        mdp = form[utils.MDP]
        try:
            return Dao().identifier_usager(nom, mdp)
        except:
            return False

    def voir_infos_usager(self, form):
        compagnies = Dao().select_all_compagnie_de_membre(form[utils.ID_MEMBRE])
        employes = []
        for compagnie in compagnies:
            nom_compagnie = Dao().select_nom_compagnie(compagnie[1])
            employes.append(Dao().select_all_membres_de_compagnie(nom_compagnie))
        return employes

    def creer_compte_ville(self, form):
        try:
            id_compagnie = Dao().insert_compagnie(form[utils.NOM_VILLE], form[utils.PAYS], form[utils.PROVINCE],
                                                  form[utils.REGION])
            id_user = self.creer_compte_admin(nom=form[utils.NOM], prenom=form[utils.PRENOM], id_compagnie=id_compagnie,
                                    genre=form[utils.GENRE], mdp_admin=form[utils.MDP],
                                    identifiant=form[utils.NOM_USAGER])
            return id_compagnie, id_user
        except:
            return "Impossible d'ajouter votre compagnie"

    def creer_usager(self, form):
        prenom = form[utils.PRENOM]
        nom = form[utils.NOM]
        identifiant = form[utils.IDENTIFIANT]
        mdp = form[utils.MDP]
        titre = form[utils.TITRE]
        genre = form[utils.GENRE]
        id_compagnie = form[utils.ID_COMPAGNIE]
        permission = form[utils.PERMISSION]
        access = form[utils.NOM_ACCES]
        return Dao().insert_membre(prenom, nom, identifiant, mdp, titre, genre, id_compagnie, permission, access)

    def creer_compte_admin(self, identifiant: str, mdp_admin: str, id_compagnie: int, genre: str, nom: str,
                           prenom: str):
        try:
            return Dao().insert_membre(prenom=prenom, nom=nom, identifiant=identifiant, mdp=mdp_admin,
                                       id_compagnie=id_compagnie, titre="admin", permission='ALL', genre=genre,
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

    def voir_compagnie_id_utilisateur(self, form):
        return Dao().select_all_compagnie_de_membre(form[utils.ID_MEMBRE])

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

    def select_modules_with_access_of_user(self, form: dict):
        return Dao().select_modules_matching_username(form[utils.NOM_USAGER])

    def get_access(self, form):
        return Dao().select_id_access(form[utils.ID_MEMBRE])

    def get_username_id(self, form):
        return Dao().select_id_membre_with_username(form[utils.NOM_USAGER])


    def get_module_with_access_id(self, form):
        return Dao().select_modules_with_access_id(form[utils.ACCESS_ID])

    def nom_compagnie(self,form):
        return Dao().select_nom_compagnie(form[utils.ID_COMPAGNIE])

    def id_compagnie(self, form):
        return Dao().select_id_of_compagnie(form[utils.NOM_COMPAGNIE])

    def get_module_id_by_user_id(self, form):
        return Dao().select_module_id_by_user_id(form[utils.IDENTIFIANT])

    def get_module_id_by_company_id(self, form):
        return Dao().select_module_id_by_company_id(form[utils.ID_COMPAGNIE])

    def add_test_data(self, form):
        return Dao().add_test_data()

if __name__ == "__main__":
    Dao().creer_bd()
    Dao().ajouter_acces_super_admin()
    Dao().ajouter_modules_initiaux()
    #Dao().ajouter_lien_acces_module_super_admin()
    pass

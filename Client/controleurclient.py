import json
import urllib.parse
import urllib.request
from sys import path
from tkinter import ttk

from Client.modules_refactor.module_ajout_membre import ModuleAjoutEmploye
from Client.modules_refactor.module_ajout_modules import ModuleAjoutModules
from Client.modules_refactor.module_gestion_ajout import ModuleGestionAjout
from Client.modules_refactor.module_gestion_des_modules import ModuleGestionDesModules
from Client.modules_refactor.module_gestion_employes import ModuleGestionEmploye
from Client.modules_refactor.module_initial import ModuleInitial
from Client.modules_refactor.module_inv import ModuleInventaire
from Client.modules_refactor.module_menu import ModuleMenu
from Client.modules_refactor.module_paiement import ModulePaiement
from Client.modules_refactor.module_vehicule import ModuleVehicule
from Client.modules_refactor.module_ventes_en_ligne import ModuleVentesEnLigne
from Utils import utils

path.append('../Utils')


# import Utils.utils as utils


# class Controleur_Client(Controleur):
class ControleurClient:
    def __init__(self):
        self.dict_modules = {
            "menu": ModuleMenu,
            "initial": ModuleInitial,
            "GestionMembre": ModuleGestionEmploye,
            "AjoutModules": ModuleAjoutModules,
            "GestionAjout":ModuleGestionAjout,
            "ModulePaiement":ModulePaiement,
            "ModuleGestionDesModules":ModuleGestionDesModules,
            "Gestion Vente En Ligne":ModuleVentesEnLigne,
            "ModuleInventaire": ModuleInventaire,
            "ModuleVehicule": ModuleVehicule,
            "ModuleAjoutEmploye":ModuleAjoutEmploye
        }

        self.dict_modules_idx = {}
        self.access = None
        self.permission: str = ""
        self.user_id: int = -1
        self.company_id: int = -1
        self.module_actuelle = None
        config = ttk.Style()
        config.configure('new.TFrame', background='dark red')
        self.master_frame = ttk.Frame(style='new.TFrame')
        self.set_module("initial")
        self.master_frame.mainloop()

    ###################################################
    def set_module(self, module: str):
        if self.module_actuelle is not None:
            self.module_actuelle.vider_vue()
        self.module_actuelle = self.dict_modules[module](self, self.master_frame)
        self.module_actuelle.show_vue()

    ###################################################

    # On pr??pare et on envoie les infos, incluant
    # le nom de la fonction, au serveur_web, qui, lui
    # les reliera au controleur_serveur qui, lui
    # communiquera avec la BD
    # La r??ponse est json-ifi??e

    def appel_serveur(self, args):
        # on encode les donn??es en format url
        # et ensuite en bytes
        data = urllib.parse.urlencode(args).encode('ascii')

        # on effectue la demande au serveur
        # reponse = urllib.request.urlopen(Controleur.URL, data)
        reponse = urllib.request.urlopen(utils.URL, data)

        # on retourne l'objet retourn?? par le serveur
        # qui avait ??t?? json-ifi??
        return json.loads(reponse.read())

    def add_test_data(self):
        infos = {utils.FONCTION: utils.ADD_TEST_DATA}
        return self.appel_serveur(infos)

    # Le nom de la fonction voulue est envoy??e
    # par le controleur_client et re??u par le
    # controleur_serveur dans le request.form
    def identifier_usager(self, nom, mdp):
        infos = {
            utils.FONCTION: utils.IDENTIFIER_USAGER,
            utils.NOM_USAGER: nom,
            utils.MDP: mdp
        }
        return self.appel_serveur(infos)

    def get_module_id_by_user_id(self):
        a = {
            utils.FONCTION: utils.GET_MODULE_ID_BY_USER_ID,
            utils.IDENTIFIANT: self.user_id
        }
        return self.appel_serveur(a)

    def get_module_id_by_company_id(self):
        a = {
            utils.FONCTION: utils.GET_MODULE_ID_BY_COMPANY_ID,
            utils.ID_COMPAGNIE: self.company_id
        }
        return self.appel_serveur(a)

    def rechercher_compagnie(self, nom_ville):
        a = {
            utils.FONCTION: utils.CHERCHER_COMPAGNIE,
            utils.NOM_VILLE: nom_ville
        }
        return self.appel_serveur(a)

    def get_employes_de_compagnie(self):
        a = {
            utils.FONCTION: utils.CHERCHER_EMPLOYES_COMPAGNIE,
            utils.ID_MEMBRE: self.user_id
        }
        return self.appel_serveur(a)

    def creer_compte_ville(self, **args_ville):
        args_ville[utils.FONCTION] = utils.CREER_COMPTE_VILLE
        return self.appel_serveur(args_ville)

    def afficher_compagnie_de_membre(self, ):
        infos = {
            utils.ID_MEMBRE: self.user_id,
            utils.FONCTION: utils.VOIR_INFOS_USAGER
        }
        return self.appel_serveur(infos)

    def afficher_membres(self):
        a = {utils.FONCTION: utils.AFFICHER_MEMBRES}

        return self.appel_serveur(a)

    def afficher_compagnies(self):
        a = {utils.FONCTION: utils.AFFICHER_COMPAGNIES}

        return self.appel_serveur(a)

    def creation_acces_admin(self):
        a = {
            utils.FONCTION: utils.NOM_ACCES,
            utils.NOM_ACCES: 'Super Administrateur'
        }
        self.appel_serveur(a)

    def creer_usager(self, prenom, nom, identification, mdp, titre, genre, compagnie, permission, acced):
        a = {
            utils.PRENOM: prenom,
            utils.NOM: nom,
            utils.IDENTIFIANT: identification,
            utils.MDP: mdp,
            utils.TITRE: titre,
            utils.GENRE: genre,
            utils.ID_COMPAGNIE: compagnie,
            utils.PERMISSION: permission,
            utils.NOM_ACCES: acced,
            utils.FONCTION: utils.CREER_USAGER
        }

        return self.appel_serveur(a)

    def ajouter_vehicule(self, annee, marque, modele, kilometrage, type, compagnie):
        a = {
            utils.ANNEE: annee,
            utils.MARQUE: marque,
            utils.IDENTIFIANT: modele,
            utils.MDP: kilometrage,
            utils.TITRE: type,
            utils.ID_COMPAGNIE: compagnie
        }

        return self.appel_serveur(a)

    def creation_modules(self):
        a = {
            utils.FONCTION: utils.AFFICHER_MODULES
        }
        return self.appel_serveur(a)

    def select_modules_with_access_of_user(self):
        a = {
            utils.FONCTION: utils.SELECT_MODULES_WITH_ACCESS_OF_USER,
            utils.NOM_USAGER: self.user_id
        }

        return self.appel_serveur(a)

    def get_module(self):
        a = {
            utils.FONCTION: utils.GET_MODULE
        }
        return self.appel_serveur(a)

    def get_all_id_compagnie_utilisateur(self, user_id):
        a = {
            utils.FONCTION: utils.VOIR_COMPAGNIE_ID_UTILISATEUR,
            utils.ID_MEMBRE: user_id
        }
        return self.appel_serveur(a)

    def get_compagnie_id(self, compagnie_name):
        a = {
            utils.FONCTION: utils.ID_COMPAGNIE,
            utils.NOM_COMPAGNIE: compagnie_name
        }
        return self.appel_serveur(a)

    def get_name_compagnie_byid(self, compagnie_id):
        a = {
            utils.FONCTION: utils.NOM_COMPAGNIE,
            utils.ID_COMPAGNIE: compagnie_id
        }
        return self.appel_serveur(a)

    def get_access(self):
        a = {
            utils.FONCTION: utils.GET_ACCESS,
            utils.ID_MEMBRE: self.user_id

        }
        return self.appel_serveur(a)

    def get_access_by_id(self, id:int):
        a = {
            utils.FONCTION: utils.GET_ACCESS,
            utils.ID_MEMBRE: id

        }
        return self.appel_serveur(a)



    def delete_membre(self, user_identifiant):
        a = {
            utils.FONCTION: utils.DELETE_MEMBRE,
            utils.IDENTIFIANT: user_identifiant
        }
        return self.appel_serveur(a)


    def get_username_id(self, username):
        a = {
            utils.FONCTION: utils.GET_USERNAME_ID,
            utils.NOM_USAGER: username
        }
        return self.appel_serveur(a)

    def get_modules_with_access(self):

        self.modules = self.appel_serveur(
            {utils.FONCTION: utils.GET_MODULE_WITH_ACCESS_ID, utils.ACCESS_ID: self.access})
        for idx, nom in self.modules:
            self.dict_modules_idx[nom] = idx

        print(self.dict_modules_idx)


# test
def main():
    c = ControleurClient()
    d = c.identifier_usager('toto', 'totototo')
    print(d)

    return 0


if __name__ == '__main__':
    quit(main())

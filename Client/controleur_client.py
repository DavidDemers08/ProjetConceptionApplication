import urllib.request
import urllib.parse
import json

from sys import path
from Utils import utils

path.append('../Utils')


# import Utils.utils as utils


# class Controleur_Client(Controleur):
class Controleur_Client:
    def __init__(self):
        self.username = None
        self.module_actuelle = None
        self.modules = {
            "login": 0

        }
        #self.set_module("login")

    def set_module(self, nom_module: str) -> None:
        if self.module_actuelle is not None:
            self.module_actuelle.vider_vue()
        self.module_actuelle = self.modules[nom_module]
        self.module_actuelle.remplir_vue()

    # On prépare et on envoie les infos, incluant
    # le nom de la fonction, au serveur_web, qui, lui
    # les reliera au controleur_serveur qui, lui
    # communiquera avec la BD
    # La réponse est json-ifiée

    def appel_serveur(self, args):
        # on encode les données en format url
        # et ensuite en bytes
        data = urllib.parse.urlencode(args).encode('ascii')

        # on effectue la demande au serveur
        # reponse = urllib.request.urlopen(Controleur.URL, data)
        reponse = urllib.request.urlopen(utils.URL, data)

        # on retourne l'objet retourné par le serveur
        # qui avait été json-ifié
        return json.loads(reponse.read())

    # Le nom de la fonction voulue est envoyée
    # par le controleur_client et reçu par le
    # controleur_serveur dans le request.form
    def identifier_usager(self, nom, mdp):
        infos = {
            utils.FONCTION: utils.IDENTIFIER_USAGER,
            utils.NOM_USAGER: nom,
            utils.MDP: mdp
        }
        return self.appel_serveur(infos)

    def rechercher_compagnie(self, nom_ville):
        a = {
            utils.FONCTION : utils.CHERCHER_COMPAGNIE,
            utils.NOM_VILLE: nom_ville
        }
        return self.appel_serveur(a)
    def creer_compte_ville(self, **args_ville):
        args_ville[utils.FONCTION] = utils.CREER_COMPTE_VILLE
        return self.appel_serveur(args_ville)

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

    def creation_modules(self):
        a = {
            utils.FONCTION: utils.AFFICHER_MODULES
        }
        return self.appel_serveur(a)

    def get_access(self):
        a = {
            utils.FONCTION: utils.GET_ACCESS
        }
        return self.appel_serveur(a)

    def get_module(self):
        a = {
            utils.FONCTION: utils.GET_MODULE
        }
        return self.appel_serveur(a)


# test
def main():
    c = Controleur_Client()
    d = c.identifier_usager('toto', 'totototo')
    print(d)

    return 0


if __name__ == '__main__':
    quit(main())

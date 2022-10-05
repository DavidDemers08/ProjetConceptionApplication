import urllib.request
import urllib.parse
import json

from sys import path

path.append('../Utils')
# import Utils.utils as utils
import utils

# class Controleur_Client(Controleur):
class Controleur_Client:
    def set_vue(self, vue):
        self.vue = vue

    def set_vue_gestion(self, vue_gestion):
        self.vue_gestion= vue_gestion


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
            utils.NOM: nom,
            utils.MDP: mdp
        }
        return self.appel_serveur(infos)

    def creer_compte_ville(self, **args_ville):

        args_ville[utils.FONCTION] = utils.CREER_COMPTE_VILLE
        print(args_ville)
        return self.appel_serveur(args_ville)


# test
def main():
    c = Controleur_Client()
    d = c.identifier_usager('toto', 'totototo')
    print(d)

    return 0


if __name__ == '__main__':
    quit(main())

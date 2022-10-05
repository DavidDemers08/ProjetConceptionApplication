from controleur_serveur import Controleur_Serveur
from serveur_web import Serveur_Web

from sys import path

path.append('../Utils')
import Utils.utils as utils


def main():
    controleur = Controleur_Serveur()

    Serveur_Web.set_controleur(controleur)
    Serveur_Web.lancer(utils.HOTE, utils.PORT)

    return 0


if __name__ == '__main__':
    quit(main())

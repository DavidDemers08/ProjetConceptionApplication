from traceback import print_exc
from tkinter import Tk
from Client.vues.vue_gestion_inventaire import VueGestionInventaire
from Client.controleur_client import Controleur_Client

class Module_Gestion(Tk):
    def __init__(self):
        super().__init__()
        controleur = Controleur_Client()

        # peut-être éventuellement dans une sous-classe
        vue_gestion_inventaire = VueGestionInventaire(self)
        vue_gestion_inventaire.grid(row=9, column=4, padx=10, pady=10)
        vue_gestion_inventaire.set_controleur(controleur)
        controleur.set_vue_gestion(vue_gestion_inventaire)

def main():
    try:
        module = Module_Gestion()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())
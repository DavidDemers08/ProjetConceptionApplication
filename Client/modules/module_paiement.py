from tkinter import Tk
from traceback import print_exc

from Client.vues.vue_paiement import VuePaiement



class ModulePaiement(Tk):
    def __init__(self):
        super().__init__()
        controleur = ControleurClient()

        vue_paiement = VuePaiement(self, controleur)
        vue_paiement.grid(row=3, column=3, padx=10, pady=10)

        controleur.set_vue(vue_paiement)


def main():
    try:
        module = ModulePaiement()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
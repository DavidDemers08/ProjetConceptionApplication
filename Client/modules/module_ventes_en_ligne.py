from traceback import print_exc
from tkinter import Tk
from Client.vue_ventes_en_ligne import VueOnlineSales
#from vue_gerer_emp import VueGererEmp
from Client.controleur_client import Controleur_Client

class Module_Ventes_En_ligne(Tk):
    def __init__(self):
        super().__init__()
        self.controleur = Controleur_Client()

        # peut-être éventuellement dans une sous-classe
        vue_ventes_en_ligne = VueOnlineSales(self)
        vue_ventes_en_ligne.grid(row=6, column=5, padx=10, pady=10)
        vue_ventes_en_ligne.set_controleur(self.controleur)
        self.controleur.set_vue_gestion(vue_ventes_en_ligne)

def main():
    try:
        module = Module_Ventes_En_ligne()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0

if __name__ == '__main__':
    quit(main())
from traceback import print_exc

from Client.AbstractClasses.Module import Module
from Client.AbstractClasses.Vue import Vue

import tkinter as tk
from tkinter import ttk


from Utils.Table import Table


class ModulePaiement(Module):

    def __init__(self, controleur, master_frame):
        super().__init__(controleur, master_frame)

    def set_vue(self):
        return ModulePaiement.VuePaiement(self, self.master_frame, row=3, column=3, padx=0, pady=0)

    class VuePaiement(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)


        def remplir_vue(self):
            #self.controleur.add_test_data() #todo enlever cette fct

            self.bouton_back = ttk.Button(self.master_frame, text='menu',
                                                command=lambda: self.clic_bouton_back())
            self.bouton_back.grid(row=0, column=0, sticky=tk.E)

            self.heading = ttk.Label(self.master_frame, text='Paiement', style='Heading.TLabel')
            self.heading.grid(column=0, row=1, columnspan=2, pady=5, sticky=tk.N)

            self.liste_module_db = self.controleur.get_module_id_by_company_id()
            if len(self.liste_module_db) != 0:
                self.module = ttk.Label(self.master_frame, text="Module")
                self.module.grid(column=0, row=2, sticky=tk.W, padx=50)
                self.prix = ttk.Label(self.master_frame, text="Prix")
                self.prix.grid(column=1, row=2, sticky=tk.W, padx=50)
                self.exp_date = ttk.Label(self.master_frame, text="Date d'expiration")
                self.exp_date.grid(column=2, row=2, sticky=tk.W, padx=50)
                self.liste_module_db.append(self.calcul_total())
                table = Table(vue=self.master_frame, lines_array=self.liste_module_db, start_row=3, start_column=0,
                              padx=50,
                              modifiable_rows=False)
                table.create()
                #self.calcul_total()
            else:
                self.exp_date = ttk.Label(self.master_frame, text="Vous avez acheter aucun module")
                self.exp_date.grid(column=0, row=2, columnspan=2, pady=5, sticky=tk.N)


        def calcul_total(self):
            total = 0
            for module in self.liste_module_db:
                total += float(module[1])
            total = round(total, 2)
            return "Total", str(total), ""

        def clic_bouton_back(self):
            self.controleur.set_module("menu")


def main():
    try:
        controleur = None
        module = ModulePaiement(controleur)
        module.show_vue()
        module.mainloop()
    except:
        print_exc()
        return 1
    return 0


if __name__ == '__main__':
    quit(main())
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
        return ModulePaiement.VuePaiement(self, self.master_frame, row=3, column=3, padx=10, pady=10)

    class VuePaiement(Vue):
        def __init__(self, parent, master_frame, row: int, column: int, padx: int, pady: int):
            super().__init__(parent, master_frame, row, column, padx, pady)

            ###test pour remplir liste module
            self.liste_module = []
            self.liste_module.append(["nom module 1", "42.45", "2001/9/11"])
            self.liste_module.append(["nom module 2", "412.45", "2001/91/11"])
            self.liste_module.append(["nom module 3", "421.45", "20011/9/11"])



        def remplir_vue(self):
            self.heading = ttk.Label(self.master_frame, text='Paiement', style='Heading.TLabel')
            self.heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)
            self.module = ttk.Label(self.master_frame, text="Module")
            self.module.grid(column=0, row=1, sticky=tk.W, padx=50)
            self.prix = ttk.Label(self.master_frame, text="Prix")
            self.prix.grid(column=1, row=1, sticky=tk.W, padx=50)
            self.exp_date = ttk.Label(self.master_frame, text="Date d'expiration")
            self.exp_date.grid(column=2, row=1, sticky=tk.W, padx=50)
            self.remplir_grid_module()
            self.calcul_total()

        def remplir_grid_module(self):
            self.liste_module.append(self.calcul_total())
            table = Table(vue=self.master_frame, lines_array=self.liste_module, start_row=2, start_column=0, padx=50,
                          modifiable_rows=False)
            table.create()

        def calcul_total(self):
            total = 0
            for module in self.liste_module:
                total += float(module[1])
            total = round(total, 2)
            return ("Total", str(total), "")



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
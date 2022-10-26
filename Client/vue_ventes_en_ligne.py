import tkinter as tk
from tkinter import ttk
import Utils.utils
from Serveur.DAO.dao import Dao
#from vue import Vue

class VueOnlineSales(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controleur = None
        # self.remplir_vue_ventes_main()
        self.rempli_vue_faire_commande()
        self.parent= parent

    def set_controleur(self, controleur):
        self.controleur = controleur

    def vider_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remplir_vue_ventes_main(self):
        self.label_tittle = ttk.Label(self,text='Ventes en ligne' )
        self.label_tittle.grid(row=0, column=1,columnspan=2)

        self.button_create_order = ttk.Button(self, text='Faire une commande' ,width = 25)
        self.button_create_order.grid(row=1, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.button_verify_order = ttk.Button(self, text='Verifier une commande',width = 25)
        self.button_verify_order.grid(row=3, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.button_complete_order = ttk.Button(self, text='Completer une commande',width = 25 )
        self.button_complete_order.grid(row=5, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

        self.button_back = ttk.Button(self, text='Retour',width = 25 )
        self.button_back.grid(row=7, column=1,columnspan=3, pady=(20, 0), sticky=tk.E)

    def rempli_vue_faire_commande(self):
        UNIT_OPTIONS = [
            "Jan",
            "Feb",
            "Mar"
        ]  # etc

        PAYMENT_OPTIONS = [
            "Visa",
            "Mastercard",
            "American Express",
            "Debit",
            "Cash"
        ]


        self.unit_options = tk.StringVar(self)
        self.unit_options.set(UNIT_OPTIONS[0])  # default value

        self.payment_options = tk.StringVar(self)
        self.payment_options.set(PAYMENT_OPTIONS[0])

        self.tittle_label = ttk.Label(self, text='Faire une commande')
        self.tittle_label.grid(row=0, column=1, columnspan=2)

        self.unit_type_label = ttk.Label(self, text="Type d'unité",width = 20, borderwidth=2, relief="groove")
        self.unit_type_label.grid(row=1, column=1,pady=(20, 0) )

        self.unit_options_dropdown = ttk.OptionMenu(self, self.unit_options, *UNIT_OPTIONS,)
        self.unit_options_dropdown.grid(row=1, column=2,pady=(20, 0), columnspan=3)

        self.price_label = ttk.Label(self, text="Prix",width = 20, borderwidth=2, relief="groove")
        self.price_label.grid(row=2, column=1, pady=(20, 0), )

        self.unit_price = ttk.Label(self, text="prixUnite", width=20, borderwidth=2, relief="groove")
        self.unit_price.grid(row=2, column=2, pady=(20, 0) )

        self.date_label = ttk.Label(self, text="Date",width = 20, borderwidth=2, relief="groove")
        self.date_label.grid(row=3, column=1,pady=(20, 0),  )

        self.date_value = ttk.Label(self, text="dateNow", width=20, borderwidth=2, relief="groove")
        self.date_value.grid(row=3, column=2, pady=(20, 0))

        self.buyer_label = ttk.Label(self, text="Acheteur",width = 20, borderwidth=2, relief="groove")
        self.buyer_label.grid(row=4, column=1,pady=(20, 0), )

        self.buyer_value = ttk.Entry(self,  width=20,  )
        self.buyer_value.grid(row=4, column=2, pady=(20, 0))

        self.payment_label = ttk.Label(self, text="Paiement",width = 20, borderwidth=2, relief="groove")
        self.payment_label.grid(row=5, column=1,pady=(20, 0),  )

        self.payment_options_dropdown = ttk.OptionMenu(self, self.payment_options, *PAYMENT_OPTIONS )
        self.payment_options_dropdown.grid(row=5, column=2, pady=(20, 0), columnspan=3)

        self.order_button  = ttk.Button(self, text='Confirmer commande', width=30, command=self.confirm_order)
        self.order_button.grid(row=6, column=1, pady=(20, 0), columnspan=2)

        self.back_button = ttk.Button(self, text='Retour')
        self.back_button.grid(row=7, column=1,pady=(20, 0), columnspan=2)

    def confirm_order(self):
        value = []
        #value['type'] = self.unit_options_dropdown.get()
        #value['price'] = self.unit_price.get()
        #value['date'] = self.date_value.get()
        value['buyer'] = self.buyer_value.get()
        #value['payment'] = self.payment_options_dropdown.get()

        print(value)




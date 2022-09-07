## -*- Encoding: UTF-8 -*-
import urllib.request
import urllib.parse 
import json 

from tkinter import *
from tkinter.simpledialog import *
from tkinter import ttk

import sys

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self.cadreapp=Frame(self.root)
        self.canevas=Canvas(self.cadreapp,width=800,height=600)
        self.canevas.create_text(400,100,anchor=CENTER,text="Bienvenue a SaaS COMMANDE")
        self.canevas.pack()
        self.listeclients=Listbox(self.canevas,width=50,height=10)
        self.canevas.create_window(400,300,anchor=CENTER,window=self.listeclients)
        self.btnclients=Button(self.canevas,text="Chercher nos client",command=self.demanderclients)
        self.canevas.create_window(400,500,anchor=CENTER,window=self.btnclients)
        self.cadreapp.pack()
        
    def demanderclients(self):
        self.parent.demanderclients()
        
    def afficherclients(self,clients):
        self.listeclients.delete(0,END)
        for i in clients:
            self.listeclients.insert(END,i)
          
class Modele():
    def __init__(self,parent,nom,compagnie):
        self.parent=parent
        self.nom=nom
        self.compagnie=compagnie

    def demanderclients(self):
        self.clients=self.parent.requeteserveur("demanderclients")
        self.clients.sort()
        listedeclients=[]
        for i in self.clients:
            listedeclients.append(i[0]+", "+i[1]+", "+i[2])
        self.parent.afficherclients(listedeclients)
        
    
class Controleur():
    def __init__(self):
        self.vue=Vue(self)
        print(sys.argv)
        self.urlserveur=sys.argv[1]
        usager=json.loads(sys.argv[2])
        self.modele=Modele(self,usager[0],usager[1])
        self.vue.root.mainloop()
    
    def requeteserveur(self,fonc):
        leurl=self.urlserveur+"/requeteserveur"
        params = {"fonction":fonc}
        reptext=self.appelserveur(leurl,params)
        rep=json.loads(reptext)
        return rep
    
    # fonction d'appel normalisee, utiliser par les methodes du controleur qui communiquent avec le serveur
    def appelserveur(self,url,params):
        query_string = urllib.parse.urlencode( params )
        data = query_string.encode( "ascii" )
        url = url + "?" + query_string 
        rep=urllib.request.urlopen(url , data)
        reptext=rep.read()
        return reptext

    def demanderclients(self):
        self.modele.demanderclients()
        
    def afficherclients(self,clients):
        self.vue.afficherclients(clients)
if __name__ == '__main__':
    c=Controleur()
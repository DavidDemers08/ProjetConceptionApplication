from tkinter import *
from tkinter.ttk import *

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        
        self.widgetsdesaisie={}
        self.cadregestion()
        
    def cadregestion(self):
        self.cadreinfo=Frame(self.root)
        self.cadreoperateurs=Frame(self.root)
        self.cadretable=Frame(self.root)
        
        self.creercadreinfo()
        self.creercadreoperateurs()
        self.creercadretable()
        
        self.cadreinfo.pack()
        self.cadreoperateurs.pack()
        self.cadretable.pack()
        
    
    def creercadretable(self):
        self.tableau=Treeview(self.cadretable)
        self.tableau.pack()
        
    def creercadreoperateurs(self):
        self.btncreercours=Button(self.cadreoperateurs,text="Enregistrer",command=self.enregistrercours)
        self.btncreercours.pack(side=LEFT)
        self.btnnbrcours=Button(self.cadreoperateurs,text="Compter les cours",command=self.compterlescours)
        self.btnnbrcours.pack(side=LEFT)
        
    def compterlescours(self):
        rep=self.parent.compterlescours()
        print("Il  a actuellement ",rep," cours dans la liste.")
        
        
    def enregistrercours(self):
        titre=self.widgetsdesaisie["titre"].get()
        id=self.widgetsdesaisie["id"].get()
        annee=self.widgetsdesaisie["annee"].get()
        session=self.widgetsdesaisie["session"].get()
        prof=self.widgetsdesaisie["prof"].get()
        print("ENREGISTRER: ", titre, id, annee, session,prof)
        listecours=self.parent.enregistrercours([titre, id, annee, session,prof])
        
        self.miseajourtableau(listecours)
        
    def miseajourtableau(self,liste):
        #efface contenu
        for i in self.tableau.get_children():
            self.tableau.delete(i)
        
        self.tableau["columns"]=("one","two","three","four","five")
        self.tableau.column('#0', width=0, minwidth=0, stretch=NO)
        self.tableau.column("one", width=150, minwidth=120, stretch=NO)
        self.tableau.column("two", width=150, minwidth=120)
        self.tableau.column("three", width=150, minwidth=120, stretch=NO)
        self.tableau.column("four", width=150, minwidth=120)
        self.tableau.column("five", width=150, minwidth=120, stretch=NO)
        
        
        self.tableau.heading("one", text="Titre")
        self.tableau.heading("two", text="id")
        self.tableau.heading("three", text="annee")
        self.tableau.heading("four", text="session")
        self.tableau.heading("five", text="prof")
        
        for i in liste:
            self.tableau.insert("", 0, text="", values=(i.titre,
                                                        i.id,
                                                        i.annee,
                                                        i.session,
                                                        i.prof))
            
        
        
    def creercadreinfo(self):
        champs=["titre","id","annee","session","prof"]
        rangee=0
        for i in champs:
            labentree=Label(self.cadreinfo,text=i)
            entree=Entry(self.cadreinfo)
            labentree.grid(row=rangee,column=0,sticky=E+W)
            entree.grid(row=rangee,column=1,sticky=E+W)
            rangee+=1
            self.widgetsdesaisie[i]=entree
              
class Cours():
    def __init__(self,parent, info):
        self.parent=parent
        #self.titre,self.id,self.annee,self.session,self.prof =info    # ceci fonctionne aussi, voir depaquetage des sequences en python
        self.titre=info[0]
        self.id=info[1]
        self.annee=info[2]
        self.session=info[3]
        self.prof=info[4]
        
class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.listecours=[]
        
    def enregistrercours(self,info):
        cours=Cours(self,info)
        self.listecours.append(cours)
        
class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def enregistrercours(self,info):
        self.modele.enregistrercours(info)
        return self.modele.listecours
        
    def compterlescours(self):
        return len(self.modele.listecours)
        
if __name__ == '__main__':
    c=Controleur()
    
    
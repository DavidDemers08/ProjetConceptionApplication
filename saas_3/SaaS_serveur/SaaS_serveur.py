#import flask
from flask import Flask,request,json
from werkzeug.wrappers import Response
import os
# pour retrouver le dossier courant d'execution
import sys

import sqlite3

app = Flask(__name__)

app.secret_key="qwerasdf1234"

class Dbclient():
    def __init__(self):
        nomdb=os.getcwd()+"/SaaS_clients/"+"GestMedia_client.sqlite"
        self.conn = sqlite3.connect(nomdb)
        self.curs = self.conn.cursor()

    def trouverprojets(self):
        sqlnom=("select Nomdeprojet, datedelancement, datedefinprevue from 'projet'")
        self.curs.execute(sqlnom)
        info=self.curs.fetchall()
        return info
    
    def trouverclients(self):
        sqlnom=("select compagnie, nom, courriel from 'client'")
        self.curs.execute(sqlnom)
        info=self.curs.fetchall()
        return info

    def fermerdb(self):
        self.conn.close()


class Dbman():
    def __init__(self):
        self.conn = sqlite3.connect("CVMJMD_clientscorpo.sqlite")
        self.curs = self.conn.cursor()

    def identifierusager(self,nom,mdp):
        sqlnom=("select * from 'membre' where identifiant=:qui and mdp=:secret")
        self.curs.execute(sqlnom, {'qui': nom, 'secret': mdp})
        info=self.curs.fetchall()

        if info:
            sqlnom=("select nomcompagnie from 'compagnie' where idcompagnie=:qui")
            self.curs.execute(sqlnom, {'qui': info[0][1]})
            co=self.curs.fetchall()
            return [info,co]
        return "inconnu"

    def trouvermembres(self):
        sqlnom=("select identifiant, permission,titre from 'membre'")
        self.curs.execute(sqlnom)
        info=self.curs.fetchall()
        return info


    def fermerdb(self):
        self.conn.close()

def demanderclients():
    db=Dbclient()
    clients=db.trouverclients()
    db.fermerdb()
    return clients
    
mesfonctions={"demanderclients":demanderclients}

@app.route('/')
def index():
    return 'Hello world du serveur '+ os.getcwd()

@app.route('/trouvermodules',methods=["GET","POST"])
def trouvermodules():
    listefichiers=[]
    monhome=os.path.dirname(os.path.realpath(sys.argv[0]))+"/SaaS_modules"
    #monhome=os.getcwd()+"/SaaS_modules"
    listefichiers=os.listdir(monhome)
    return Response(json.dumps(listefichiers), mimetype='application/json')

@app.route('/telechargermodule', methods=["GET","POST"])
def telechargermodule():
    if request.method=="POST":
        fichier=request.form["fichier"]
        monhome=os.path.dirname(os.path.realpath(sys.argv[0]))+"/SaaS_modules"
        bonfichier=open(monhome+"/"+fichier)
        lemodule=bonfichier.read()
        bonfichier.close()
        return Response(json.dumps(lemodule), mimetype='application/json')
        #return repr(usager)
    else:
        return repr("pas ok")

@app.route('/identifierusager', methods=["GET","POST"])
def identifierusager():
    if request.method=="POST":
        nom=request.form["nom"]
        mdp=request.form["mdp"]
        db=Dbman()
        usager=db.identifierusager(nom,mdp)

        db.fermerdb()
        return Response(json.dumps(usager), mimetype='application/json')
        #return repr(usager)
    else:
        return repr("pas ok")

@app.route('/trouverprojets', methods=["GET","POST"])
def trouverprojets():
    if request.method=="POST":
        db=Dbclient()
        projets=db.trouverprojets()
        #db=Dbman()
        #projets=db.trouvermembres()
        db.fermerdb()
        return Response(json.dumps(projets), mimetype='application/json')
        #return repr(usager)
    else:
        return repr("pas ok")

@app.route('/trouvermembres', methods=["GET","POST"])
def trouvermembres():
    if request.method=="POST":
        db=Dbman()
        membres=db.trouvermembres()

        db.fermerdb()
        return Response(json.dumps(membres), mimetype='application/json')
        #return repr(usager)
    else:
        return repr("pas ok")
    
@app.route('/requeteserveur', methods=["GET","POST"])
def requeteserveur():
    if request.method=="POST":
        nomfonction=request.form["fonction"]
        rep=mesfonctions[nomfonction]()
        n=1
        return Response(json.dumps(rep), mimetype='application/json')
        #return repr(usager)
    else:
        return repr("pas ok")
if __name__ == '__main__':
    #print(flask.__version__)
    #app.run(debug=True)
    app.run(debug=True, host='127.0.0.1', port=5000)

import sqlite3

FK_ON = 'PRAGMA foreign_keys = 1'

BD_GEST_MEDIA = 'gestion_media.db'

# ***************** MEMBRE *********************

CREER_MEMBRE = '''
CREATE TABLE IF NOT EXISTS membre
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom TEXT NOT NULL,
    identifiant TEXT NOT NULL,
    mdp TEXT,
    titre TEXT,
    genre TEXT
)
'''
DROP_MEMBRE = 'DROP TABLE IF EXISTS membre'
INSERT_MEMBRE = 'INSERT INTO membre(prenom, nom, identifiant, mdp, titre,genre) VALUES(?, ?, ?, ?, ?, ?)'
SELECT_MEMBRE = 'SELECT * FROM membre'
SELECT_ID_MEMBRE = 'SELECT id FROM membre WHERE identifiant=?'
DELETE_MEMBRE = 'DELETE FROM membre WHERE identifiant=?'
UPDATE_MEMBRE = ''' 
UPDATE membre
    SET prenom = ?,
    nom = ?,
    titre = ?,
    identifiant = ?
WHERE id = ?
'''

# ***************** COMPAGNIE *********************

CREER_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT UNIQUE,
    pays TEXTE,
    province TEXTE,
    region TEXTE
)
'''
DROP_COMPAGNIE = 'DROP TABLE IF EXISTS compagnie'
INSERT_COMPAGNIE = 'INSERT INTO compagnie(nom, pays, province, region) VALUES(?, ?, ?, ?)'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie'

SELECT_ID_COMPAGNIE = 'SELECT id FROM compagnie WHERE nom =?'

# ***************** MEMBRE DANS COMPAGNIE *********************

CREER_MEMBRE_DANS_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS membre_dans_compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_compagnie INTEGER NOT NULL,
    id_membre INTEGER NOT NULL,
    permission_membre TEXT NOT NULL,
    
    FOREIGN KEY(id_compagnie) REFERENCES compagnie(id),
    FOREIGN KEY(id_membre) REFERENCES membre(id)
)
'''
DROP_MEMBRE_DANS_COMPAGNIE = 'DROP TABLE IF EXISTS membre_dans_compagnie'
INSERT_MEMBRE_DANS_COMPAGNIE = 'INSERT INTO membre_dans_compagnie(id_compagnie, id_membre, permission_membre) VALUES(?, ?, ?)'
SELECT_MEMBRE_DANS_COMPAGNIE = 'SELECT * FROM membre_dans_compagnie'
DELETE_MEMBRE_FROM_COMPAGNIE = 'DELETE FROM membre_dans_compagnie WHERE id_membre=?'
UPDATE_PERMISSION_MEMBRE = '''
UPDATE membre_dans_compagnie
    SET permission_membre = ?
WHERE id_membre = ? AND id_compagnie = ?
'''

# ***************** MODULES *********************

CREER_MODULE = '''
CREATE TABLE IF NOT EXISTS modules
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL,
    description TEXT,
    version NUMERIC NOT NULL,
    chemin_executable TEXT NOT NULL,
    prix_mensuel NUMERIC NOT NULL,
    
    UNIQUE(nom,version)
)
'''
DROP_MODULES = 'DROP TABLE IF EXISTS modules'
INSERT_MODULES = 'INSERT INTO modules(nom,description, version,chemin_executable, prix_mensuel) VALUES(?, ?, ?, ?, ?)'
# TODO Si le Select_ID ne contient pas de valeur ajuster pour qu'il puisse compiler
SELECT_ID_MODULE = 'SELECT id FROM modules WHERE nom =? AND version =?'
SELECT_MODULE_PAR_ID = 'SELECT nom,version,chemin_executable FROM modules WHERE id =? AND version =?'
SELECT_MODULES = 'SELECT * FROM modules'


class Dao:
    __creer = [
        CREER_COMPAGNIE,
        CREER_MEMBRE,
        CREER_MODULE,
        CREER_MEMBRE_DANS_COMPAGNIE
    ]
    __detruire = [
        DROP_MEMBRE_DANS_COMPAGNIE,
        DROP_MEMBRE,
        DROP_COMPAGNIE,
        DROP_MODULES

    ]

    # singleton pas possible car:

    # sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 12960 and this is thread id 14996.
    def __init__(self):
        self.chemin_bd = BD_GEST_MEDIA
        self.connexion()

    def __del__(self):
        self.deconnexion()

    def connexion(self):
        self.conn = sqlite3.connect(self.chemin_bd)
        self.cur = self.conn.cursor()
        self.cur.execute(FK_ON)

    def deconnexion(self):
        self.cur.close()
        self.conn.close()

    def creer_bd(self):
        for table in Dao.__detruire:
            self.cur.execute(table)
        for table in Dao.__creer:
            self.cur.execute(table)

    # ***************** AJOUTER METHODES DA0 *********************
    def insert_membre(self, prenom, nom, identifiant, mdp, titre, genre, id_compagnie, permission):
        cursor = self.cur.execute(INSERT_MEMBRE, (prenom, nom, identifiant, mdp, titre, genre))
        self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, cursor.lastrowid, permission))
        self.conn.commit()

    def insert_compagnie(self, nom, pays, province, region):
        self.cur.execute(INSERT_COMPAGNIE, (nom, pays, province, region))
        self.conn.commit()
        # TODO j'ai besoin de l'ID de la compagnie pour ajouter l'admin
        return self.select_all_compagnies()

    def insert_membre_dans_compagnie(self, id_compagnie, id_membre, permission_membre):
        self.cur.execute(INSERT_MEMBRE_DANS_COMPAGNIE, (id_compagnie, id_membre, permission_membre))
        self.conn.commit()

    def select_id_of_compagnie(self,name):
        self.cur.execute(SELECT_ID_COMPAGNIE, (name,))
        return self.cur.fetchall()[0][0]

    def get_membre_id(self, identifiant):
        self.cur.execute(SELECT_ID_MEMBRE, (identifiant,))
        return self.cur.fetchall()[0][0]

    def delete_membre(self, identifiant):
        id_membre = self.get_membre_id(identifiant)
        self.cur.execute(DELETE_MEMBRE_FROM_COMPAGNIE, (id_membre,))
        self.cur.execute(DELETE_MEMBRE, (identifiant,))

    def select_all_membres(self):
        self.cur.execute(SELECT_MEMBRE)
        return self.cur.fetchall()

    def select_all_compagnies(self):
        self.cur.execute(SELECT_COMPAGNIE)
        return self.cur.fetchall()

    def select_membres_all_compagnie(self):
        self.cur.execute(SELECT_MEMBRE_DANS_COMPAGNIE)
        return self.cur.fetchall()

    def identifier_usager(self, nom, mdp):
        sql = '''
            SELECT
                membre.identifiant,
                membre.titre,
                compagnie.id,
                compagnie.nom
            FROM membre
            INNER JOIN membre_dans_compagnie
                ON membre_dans_compagnie.id_membre = membre.id
            INNER JOIN compagnie
                ON membre_dans_compagnie.id_compagnie = compagnie.id
            WHERE membre.identifiant = ? AND membre.mdp = ?
        '''
        self.cur.execute(sql, (nom, mdp))
        return self.cur.fetchall()

    def update_membre(self, identifiant, nom, prenom, titre, permission_membre=None, nom_compagnie=None):
        id_membre = self.get_membre_id(identifiant)
        if (permission_membre is not None) and (nom_compagnie is not None):
            self.update_permission_membre(id_membre, nom_compagnie, permission_membre)

        self.cur.execute(UPDATE_MEMBRE, (nom, prenom, titre, identifiant, id_membre))
        self.conn.commit()

    def update_permission_membre(self, id_membre, nom_compagnie, permission_membre):
        id_compagnie = self.select_id_of_compagnie(nom_compagnie)
        self.cur.execute(UPDATE_PERMISSION_MEMBRE, (permission_membre, id_membre, id_compagnie))
        self.conn.commit()

    def insert_module(self, nom, version, prix_mensuel,chemin_executable, derscription = "Aucune Description"):
        self.cur.execute(INSERT_MODULES, (nom,derscription, version,chemin_executable,prix_mensuel))
        self.conn.commit()

    def select_all_modules(self):
        self.cur.execute(SELECT_MODULES)
        return self.cur.fetchall()

    # TODO Si le Select_ID ne contient pas de valeur ajuster pour qu'il puisse compiler
    def get_module_id(self, nom,version):
        self.cur.execute(SELECT_ID_MODULE, (nom,version,))
        return self.cur.fetchall()[0][0]

    def select_module(self, id_module, version_module):
        self.cur.execute(SELECT_MODULE_PAR_ID,(id_module,version_module))
        return self.cur.fetchall()

def main():
    Dao().creer_bd()
    return 0

# main

if __name__ == '__main__':
    quit(main())

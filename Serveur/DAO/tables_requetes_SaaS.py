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

SELECT_MEMBRES = 'SELECT * FROM membre'
SELECT_MEMBRE = 'SELECT * FROM membre WHERE identifiant=?'
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

SELECT_COMPAGNIES = 'SELECT * FROM compagnie'
SELECT_COMPAGNIE = 'SELECT * FROM compagnie WHERE id=?'
SELECT_ID_COMPAGNIE = 'SELECT id FROM compagnie WHERE nom=?'
DELETE_COMPAGNIE = 'DELETE FROM compagnie WHERE id=?'

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

SELECT_ENTIRE_MEMBRE_DANS_COMPAGNIE = 'SELECT * FROM membre_dans_compagnie'
SELECT_ALL_COMPAGNIES_DE_MEMBRE = 'SELECT * FROM membre_dans_compagnie WHERE id_membre=?'
SELECT_ALL_MEMBRES_DE_COMPAGNIE = 'SELECT * FROM membre_dans_compagnie WHERE id_compagnie=?'
SELECT_ID_FROM_MEMBRE_DE_COMPAGNIE = 'SELECT id FROM membre_dans_compagnie WHERE id_membre=? AND id_compagnie=?'
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
SELECT_MODULE = 'SELLECT * FROM modules WHERE id=?'
SELECT_MODULE_ID = 'SELECT id FROM modules WHERE nom=? AND version=?'
DELETE_MODULE = 'DELETE FROM modules WHERE nom=? AND version=?'

# ***************** MODULE PAR COMPAGNIE*********************

CREER_MODULE_PAR_COMPAGNIE = '''
CREATE TABLE IF NOT EXISTS module_par_compagnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_compagnie  INTEGER NOT NULL,
    id_module INTEGER NOT NULL,

    FOREIGN KEY(id_module) REFERENCES modules(id),
    FOREIGN KEY(id_compagnie) REFERENCES compagnie(id)
)
'''
DROP_MODULE_PAR_COMPAGNIE = 'DROP TABLE IF EXISTS module_par_compagnie'
INSERT_MODULE_PAR_COMPAGNIE = 'INSERT INTO module_par_compagnie(id_compagnie, id_module) VALUES(?,?)'

SELECT_ALL_MODULE_PAR_ALL_COMPAGNIE = 'SELECT * FROM module_par_compagnie'
SELECT_ALL_MODULE_PAR_COMPAGNIE = 'SELECT * FROM module_par_compagnie WHERE id_compagnie=?'

DELETE_ACCESS_POUR_COMPAGNIE = 'DELETE FROM module_par_compagnie WHERE id_module=? AND id_compagnie=?'


# ***************** ACCÈS *********************
CREER_ACCESS = '''
CREATE TABLE IF NOT EXISTS access
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT NOT NULL UNIQUE
)
'''
DROP_ACCESS = 'DROP TABLE IF EXISTS access'
INSERT_ACCESS = 'INSERT INTO access(nom) VALUES(?)'

SELECT_ALL_ACCESS = 'SELECT * FROM access'
SELECT_ACCESS = 'SELECT * FROM access WHERE id=?'
SELECT_ACCESS_ID = 'SELECT id FROM access WHERE nom=?'
DELETE_ACCESS = 'DELETE FROM access WHERE nom=? AND id=?'

# ***************** MODULE PAR ACCÈS *********************
CREER_MODULE_PAR_ACCESS = '''
CREATE TABLE IF NOT EXISTS module_par_access
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_module  INTEGER NOT NULL,
    id_access INTEGER NOT NULL,

    FOREIGN KEY(id_module) REFERENCES modules(id),
    FOREIGN KEY(id_access) REFERENCES access(id)
)
'''
DROP_MODULE_PAR_ACCESS = 'DROP TABLE IF EXISTS module_par_access'
INSERT_MODULE_PAR_ACCESS = 'INSERT INTO module_par_access(id_module, id_access) VALUES(?,?)'

SELECT_ALL_MODULE_PAR_ALL_ACCESS = 'SELECT * FROM module_par_access'
SELECT_ALL_MODULE_PAR_ACCESS = 'SELECT * FROM module_par_access WHERE id_access=?'
DELETE_ACCESS_POUR_MODULE = 'DELETE FROM module_par_access WHERE id_module=? AND id_access=?'

# ***************** ACCÈS PAR MEMBRE *********************
CREER_ACCESS_PAR_MEMBRE = '''
CREATE TABLE IF NOT EXISTS access_par_membre
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_membre  INTEGER NOT NULL,
    id_access INTEGER NOT NULL,

    FOREIGN KEY(id_membre) REFERENCES membre(id),
    FOREIGN KEY(id_access) REFERENCES access(id)
)
'''
DROP_ACCESS_PAR_MEMBRE = 'DROP TABLE IF EXISTS access_par_membre'
INSERT_MEMBRE_A_ACCESS = 'INSERT INTO access_par_membre(id_membre, id_access) VALUES(?,?)'

SELECT_ALL_ACCES_POUR_ALL_MEMBRES = 'SELECT * FROM access_par_membre'
SELECT_ALL_MEMBRES_POUR_ACCESS = 'SELECT * FROM access_par_membre WHERE id_access=?'
DELETE_ACCESS_POUR_MEMBRE = 'DELETE FROM access_par_membre WHERE id_membre=? AND id_access=?'
SELECT_ID_MEMBRE_WITH_USERNAME = 'SELECT id FROM membre WHERE identifiant = ?'

# ***************** CLIENT *********************
CREER_CLIENT = '''
CREATE TABLE IF NOT EXISTS client
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    courriel TEXT,
    tel TEXT,
    compagnie TEXT,
    adresse TEXT,
    rue TEXT,
    ville TEXT
)'''
DROP_CLIENT = 'DROP TABLE IF EXISTS client'
INSERT_CLIENT = 'INSERT INTO client(nom, courriel, tel, compagnie, adresse, rue, ville) VALUES(?, ?, ?, ?, ?, ?, ?)'
SELECT_CLIENT = 'SELECT * FROM client'

# ***************** PROJET *********************
CREER_PROJET = '''
CREATE TABLE IF NOT EXISTS projet
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT UNIQUE,
    client NUMERIC,
    chargedeprojet NUMERIC,
    datedelancement DATE,
    datedefinprevue DATE
)'''
DROP_PROJET = 'DROP TABLE IF EXISTS projet'
INSERT_PROJET = 'INSERT INTO projet(nomdeprojet, client, chargedeprojet, datedelancement, datedefinprevue) VALUES(?, ?, ?, ?, ?)'
SELECT_PROJET = 'SELECT * FROM projet'

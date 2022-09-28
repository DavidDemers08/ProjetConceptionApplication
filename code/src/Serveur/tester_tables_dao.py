from dao import Dao

def insert(dao):
    dao.insert_compagnie('Totologie')
    dao.insert_compagnie('Tatalogie')

    dao.insert_membre(2, 'toto', 'totototo', 'admin', 'mr')
    dao.insert_membre(1, 'tata', 'tatatata', 'user', 'mrs')

def select(dao):
    print('\nCompagnie')
    for rangee in dao.select_compagnie():
        print(rangee)
        
    print('\nMembre')
    for rangee in dao.select_membre():
        print(rangee)

def main():
    bd = Dao()
    insert(bd)
    select(bd)

    print('\nIdentifier l\'usager')
    print(bd.identifier_usager('toto', 'totototo'))

    return 0

if __name__ == '__main__':
    quit(main())
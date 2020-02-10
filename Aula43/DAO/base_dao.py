
import sqlalchemy as db


class BaseDAO:

    def __init__(self):
        conexao = db.create_engine(f'mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01')
        create_party = db.orm.sessionmaker()
        create_party.configure(bind=conexao)
        self.party = create_party()

    def conversor(self, lista):
        retorno = {}
        i = 0
        for classe in lista:
            retorno[i] = classe.as_dict()
            i += 1

        return retorno

    def list_all(self, model):
        lista_classes = self.party.query(model).all()
        return self.conversor(lista_classes)

    def get_id(self, model, id):
        query = self.party.query(model).filter(model.id.like(f'%{id}'))
        classe = query.first()
        if classe is None:
            return f"ID não encontrado"

        return classe.as_dict()

    def insert(self, objeto) -> object:
        self.party.add(objeto)
        self.party.commit()
        return objeto

    def update(self, objeto) -> object:
        self.party.merge(objeto)
        self.party.commit()
        return objeto

    def remove(self, model, id):
        query = self.party.query(model).filter(model.id == id).first()
        self.party.delete(query)
        self.party.commit()
        return f"Removendo objeto com id {id}"

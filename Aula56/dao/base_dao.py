import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

class BaseDao:
    def __init__(self, table):
        self.table = table
        engine = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        session_mk = sessionmaker()
        session_mk.configure(bind=engine)
        self.session = session_mk()

    def list_all(self):
        list = []
        list_model = self.session.query(self.table).all()
        for m in list_model:
            list.append(m.as_dict())

        return list

    def get_by_id(self, id):
        return self.session.query(self.table).filter_by(id=id).one().as_dict()

    def insert(self, model):
        self.session.add(model)
        self.session.commit()
        return f"objeto inserido com sucesso! id = {model.id}"

    def update(self, model):
        self.session.merge(model)
        self.session.commit()
        return f"objeto alterado com sucesso! objeto :{model.as_dict()}"

    def delete(self, id):
        self.session.delete(self.get_by_id(id))
        self.session.commit()
        return f"objeto deletado com sucesso!"

from flask_restful import Resource


class BaseController(Resource):

    def __init__(self, db):
        self.db = db

    def get(self, id=None):
        if id:
            return self.db.get_id(id)

        result = self.db.list_all()
        return result

    def delete(self, id):
        return self.db.remove(id)

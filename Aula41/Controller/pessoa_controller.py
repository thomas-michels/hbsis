
from flask_restful import Resource
from DAO.pessoa_dao import PessoaDAO
from Model.pessoa import Pessoa


class PessoaController(Resource):

    def __init__(self):
        self.pessoaDao = PessoaDAO()

    def get(self, id=None):
        if id:
            result = self.pessoaDao.get_id(id)
            return result

        return self.pessoaDao.list_all()

    def post(self):
        result = self.pessoaDao.insert("Pessoa")
        return result

    def put(self):
        result = self.pessoaDao.update("Pessoa 1")
        return result

    def delete(self):
        result = self.pessoaDao.remove(3)
        return result


import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula41')
from flask_restful import Resource, request
from DAO.pessoa_dao import PessoaDAO
from Model.pessoa import Pessoa


class PessoaController(Resource):

    def __init__(self):
        self.pessoaDao = PessoaDAO()

    def get(self, id=None):
        if id:
            result = self.pessoaDao.get_id(id)
            return result

        retorno = self.pessoaDao.list_all()
        return retorno

    def post(self):
        pessoa = Pessoa()
        pessoa.nome = request.json['nome']
        pessoa.id_endereco = request.json['id_endereco']
        result = self.pessoaDao.insert(pessoa)
        return result

    def put(self, id):
        pessoa = Pessoa()
        pessoa.id = id
        pessoa.nome = request.json['nome']
        pessoa.id_endereco = request.json['id_endereco']
        result = self.pessoaDao.update(pessoa)
        return result

    def delete(self, id):
        result = self.pessoaDao.remove(id)
        return result

if __name__ == '__main__':
    pc = PessoaController()
    a = pc.get()
    for i in a:
        print(i)
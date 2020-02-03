
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula41/arquivos')
from flask_restful import Resource, request
from DAO.cerveja_dao import CervejaDAO
from Model.cerveja import Cerveja


class CervejaController(Resource):

    def __init__(self):
        self.cd = CervejaDAO()

    def get(self, id=None):
        if id:
            result = self.cd.get_id(id)
            return result

        retorno = self.cd.list_all()
        return retorno

    def post(self):
        cerveja = Cerveja()
        cerveja.marca = request.json['marca']
        cerveja.abv = request.json['abv']
        cerveja.ibu = request.json['ibu']
        cerveja.ebc = request.json['ebc']
        result = self.cd.insert(cerveja)
        return result

    def put(self, id):
        cerveja = Cerveja()
        cerveja.id = id
        cerveja.marca = request.json['marca']
        cerveja.abv = request.json['abv']
        cerveja.ibu = request.json['ibu']
        cerveja.ebc = request.json['ebc']
        result = self.cd.update(cerveja)
        return result

    def delete(self, id):
        result = self.cd.remove(id)
        return result

if __name__ == '__main__':
    pc = PessoaController()
    a = pc.get()
    for i in a:
        print(i)
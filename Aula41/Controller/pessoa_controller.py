
from flask_restful import Resource

class PessoaController(Resource):

    def get(self):
        return 'Metodo - GET'

    def post(self):
        return 'Metodo - POST'

    def put(self):
        return 'Metodo - PUT'

    def delete(self):
        return 'Metodo - Delete'
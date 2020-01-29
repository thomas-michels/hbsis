from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
        return 'Controller Cerveja - GET'

    def post(self):
        return 'Metodo - POST'

    def put(self):
        return 'Metodo - PUT'

    def delete(self):
        return 'Metodo - Delete'
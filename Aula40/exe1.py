
from flask import Flask
from flask_restful import Api
from Controller.cerveja_controller import CervejaController

# GET - Busca o dado
# POST - Envia dados
# PUT - Envia dados no cabecalho e url
# DELETE - deleta

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')


@app.route('/')
def inicio():
    return 'Teste API'


app.run(debug=True)

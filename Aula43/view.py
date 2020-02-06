
from flask import Flask
from flask_restful import Api
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula41/arquivos')
from Controller.cerveja_controller import CervejaController
from Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/cerveja', endpoint='cervejas')
api.add_resource(CervejaController, '/cerveja/<int:id>', endpoint='cerveja')
api.add_resource(PessoaController, '/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/pessoa/<int:id>', endpoint='pessoa')


@app.route('/')
def inicio():
    return 'Cerveja - API'


app.run(debug=True)

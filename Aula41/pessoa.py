
from flask import Flask
from flask_restful import Api
from Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/pessoa/<int:id>', endpoint='pessoa')


@app.route('/')
def inicio():
    return 'Teste Pessoa - API'


app.run(debug=True)

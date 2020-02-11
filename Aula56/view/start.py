
from flask import Flask
from flask_restful import Api

from hbsis.Aula56.controller.autor_controller import AutorController
from hbsis.Aula56.controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(AutorController, '/api/autor', endpoint='autores')
api.add_resource(AutorController, '/api/autor/<int:id>', endpoint='autor')

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')

app.run(debug=True)

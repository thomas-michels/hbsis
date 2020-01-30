
from flask import Flask
from flask_restful import Api
from Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api')


@app.route('/')
def inicio():
    return 'Teste Pessoa - API'


app.run(debug=True)
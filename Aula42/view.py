
from flask import Flask
from flask_restful import Api
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula42')
from Controller.cerveja_controller import CervejaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/cerveja', endpoint='pessoas')
api.add_resource(CervejaController, '/cerveja/<int:id>', endpoint='pessoa')

@app.route('/')
def inicio():
    return 'Cerveja - API'


app.run(debug=True)
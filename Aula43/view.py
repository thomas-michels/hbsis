
from flask import Flask
from flask_restful import Api
import sys
sys.path.append('C:/Users/900164/Documents/hbsis/hbsis/Aula43')
from Controller.cerveja_controller import CervejaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/cerveja', endpoint='cervejas')
api.add_resource(CervejaController, '/cerveja/<int:id>', endpoint='cerveja')


@app.route('/')
def inicio():
    return 'Cerveja - API'


app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")

def inicio():
    return "Hello world"

app.run()
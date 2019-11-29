from flask import Flask, render_template
import musica

app = Flask(__name__)

@app.route('/')
def listar_faixas():
    return render_template("principal.html")

@app.route('/playlist')
def ver_playlist():
    return render_template("playlist.html", playlist = musica.ler())

@app.route('/cadastrar')
def cadastrar():
    return render_template("cadastrar.html", musica = musica.cadastrar())

app.run(debug=True)

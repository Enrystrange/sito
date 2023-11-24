from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def index():
    return f'<h1>Ciao! In questa pagina puoi generare una password casuale!</h1><a href="/pass">Vedi una password casuale!</a><a href="/coin">tira una moneta!</a>'

@app.route("/pass")

def gen_pass():
    elements = "+-/*!&$#?=@<>"
    
    return f'<p>{elements}</p>'
@app.route("/coin")
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "TESTA"
    elif flip == 1:
        return "CROCE"
    
app.run(debug=True)

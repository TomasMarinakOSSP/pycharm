import string
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kontakt")
def kontakt():
    return """
        <h1>Toto je kontaktní stránka.</h1>
        <p><a href="/">Domů</a></p>
        <p><a href="/kontakt">Kontakt</a></p>
    """


@app.route("/<jmeno>")
def hello(jmeno):
    return f"Hello {jmeno}!"

@app.route("/<cislo1>/<cislo2>")
def dve_cisla(cislo1, cislo2):
    try:
        return f"Násobek je {int(cislo1) * int(cislo2)}"
    except ValueError:
        return "neplatné čísla"



if __name__ == "__main__":
    app.run(debug=True)

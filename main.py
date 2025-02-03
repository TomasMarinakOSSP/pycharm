from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <h1>Hello World!</h1>
        <p><a href="/">Domů</a></p>
        <p><a href="/kontakt">Kontakt</a></p>
    """


@app.route("/kontakt")
def kontakt():
    return """
        <h1>Toto je kontaktní stránka.</h1>
        <p><a href="/">Domů</a></p>
        <p><a href="/kontakt">Kontakt</a></p>
    """


if __name__ == "__main__":
    app.run(debug=True)


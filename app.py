from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Servidor funcionando correctamente"


if name == "__main__":
    app.run(debug=True)
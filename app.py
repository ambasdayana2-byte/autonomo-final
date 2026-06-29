from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Variables para almacenar el puntaje del juego
puntaje_usuario = 0
puntaje_computadora = 0
empates = 0


def obtener_jugada_computadora():
    """
    Esta función devuelve una opción aleatoria para la computadora.
    Aquí se usa una lista, que es una estructura de datos.
    """
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)


def determinar_ganador(jugada_usuario, jugada_computadora):
    """
    Esta función compara la jugada del usuario con la jugada
    de la computadora y devuelve el resultado.
    """

    if jugada_usuario == jugada_computadora:
        return "Empate"

    elif jugada_usuario == "piedra" and jugada_computadora == "tijera":
        return "Ganaste"

    elif jugada_usuario == "papel" and jugada_computadora == "piedra":
        return "Ganaste"

    elif jugada_usuario == "tijera" and jugada_computadora == "papel":
        return "Ganaste"

    else:
        return "Perdiste"


@app.route("/")
def inicio():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje_error = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "admin" and password == "1234":
            return redirect(url_for("menu"))
        else:
            mensaje_error = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje_error=mensaje_error)


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/reglas")
def reglas():
    return render_template("reglas.html")


@app.route("/juego", methods=["GET", "POST"])
def juego():
    global puntaje_usuario, puntaje_computadora, empates

    jugada_usuario = ""
    jugada_computadora = ""
    resultado = ""

    if request.method == "POST":
        jugada_usuario = request.form["jugada"]
        jugada_computadora = obtener_jugada_computadora()
        resultado = determinar_ganador(jugada_usuario, jugada_computadora)

        if resultado == "Ganaste":
            puntaje_usuario = puntaje_usuario + 1

        elif resultado == "Perdiste":
            puntaje_computadora = puntaje_computadora + 1

        else:
            empates = empates + 1

    return render_template(
        "juego.html",
        jugada_usuario=jugada_usuario,
        jugada_computadora=jugada_computadora,
        resultado=resultado,
        puntaje_usuario=puntaje_usuario,
        puntaje_computadora=puntaje_computadora,
        empates=empates
    )


@app.route("/reiniciar")
def reiniciar():
    global puntaje_usuario, puntaje_computadora, empates

    puntaje_usuario = 0
    puntaje_computadora = 0
    empates = 0

    return redirect(url_for("juego"))


if __name__ == "__main__":
    app.run(debug=True)
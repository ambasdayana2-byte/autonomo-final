# Juego Piedra, Papel o Tijera con Python

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un juego interactivo de **Piedra, Papel o Tijera**, creado con **Python 3.13** y una interfaz gráfica web usando **HTML, CSS y JavaScript**.

El programa simula un inicio de sesión básico, muestra un menú principal con las opciones del sistema, permite consultar las reglas del juego, iniciar una partida contra la computadora y finalizar el juego.

La computadora realiza su jugada mediante un algoritmo aleatorio, mientras que el usuario selecciona una de las tres opciones disponibles: piedra, papel o tijera. Luego, el programa compara ambas jugadas y muestra el resultado: victoria, derrota o empate.

Este proyecto fue desarrollado con una estructura sencilla, ideal para aplicar conocimientos básicos de programación como variables, tipos de datos, operadores, condicionales, bucles, listas, funciones y estructuras de decisión.

---

## Objetivo general

Desarrollar un juego funcional de Piedra, Papel o Tijera utilizando Python como lenguaje principal y tecnologías web para la interfaz gráfica.

---

## Objetivos específicos

* Simular un inicio de sesión básico.
* Crear un menú principal con opciones simples.
* Mostrar las reglas del juego.
* Permitir que el usuario seleccione piedra, papel o tijera.
* Generar una jugada aleatoria para la computadora.
* Comparar la jugada del usuario con la jugada de la computadora.
* Mostrar el resultado de cada ronda.
* Llevar un puntaje de victorias, derrotas y empates.
* Aplicar conceptos básicos de programación vistos en clase.

---

## Tecnologías utilizadas

* **Python 3.13**: lenguaje principal del proyecto.
* **Flask**: framework utilizado para conectar Python con las páginas HTML.
* **HTML5**: estructura de las páginas del sistema.
* **CSS3**: estilos visuales de la interfaz.
* **JavaScript**: apoyo básico para la interfaz del usuario.
* **Visual Studio Code**: editor de código utilizado para el desarrollo.
* **Git y GitHub**: control de versiones y almacenamiento del proyecto.

---

## Funcionalidades principales

El sistema cuenta con las siguientes funcionalidades:

1. **Inicio de sesión simulado**

   El usuario debe ingresar credenciales básicas para acceder al menú principal.

   Credenciales de prueba:

   ```txt
   Usuario: admin
   Contraseña: 1234
   ```

2. **Menú principal**

   Después de iniciar sesión correctamente, el usuario accede a un menú con tres opciones:

   ```txt
   1. Reglas del juego
   2. Iniciar juego
   3. Finalizar juego
   ```

3. **Reglas del juego**

   Se muestra una página donde se explican las reglas básicas:

   ```txt
   Piedra gana contra tijera.
   Papel gana contra piedra.
   Tijera gana contra papel.
   Si ambos eligen lo mismo, es empate.
   ```

4. **Inicio del juego**

   El usuario puede escoger una de las siguientes opciones:

   ```txt
   Piedra
   Papel
   Tijera
   ```

   Luego, la computadora elige una opción aleatoria y el programa determina el resultado.

5. **Puntaje**

   El juego muestra:

   ```txt
   Puntaje del usuario
   Puntaje de la computadora
   Número de empates
   ```

6. **Reinicio del puntaje**

   El usuario puede reiniciar los puntos acumulados durante la partida.

7. **Finalización del juego**

   El usuario puede salir del juego y regresar a la pantalla de inicio de sesión.

---

## Estructura del proyecto

La estructura del proyecto es la siguiente:

```txt
piedra-papel-tijera-python/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── menu.html
│   ├── reglas.html
│   └── juego.html
│
└── static/
    ├── css/
    │   └── styles.css
    │
    └── js/
        └── script.js
```

---

## Explicación de los archivos

### `app.py`

Este es el archivo principal del proyecto. Contiene todo el código de Python necesario para ejecutar el servidor Flask y manejar la lógica del juego.

En este archivo se encuentran:

* La creación de la aplicación Flask.
* Las rutas principales del sistema.
* La validación del login.
* La lógica del juego.
* Las funciones para generar la jugada de la computadora.
* Las funciones para determinar el ganador.
* Las variables de puntaje.

Este archivo es el más importante del proyecto porque conecta la interfaz web con la lógica de programación.

---

### `requirements.txt`

Este archivo contiene las dependencias necesarias para ejecutar el proyecto.

Por ejemplo:

```txt
Flask
```

Sirve para que otra persona pueda instalar fácilmente las librerías necesarias usando:

```bash
pip install -r requirements.txt
```

---

### `README.md`

Es el archivo de documentación del proyecto. Explica qué hace el programa, cómo está organizado, qué tecnologías utiliza y cómo ejecutarlo.

---

### Carpeta `templates/`

Esta carpeta contiene los archivos HTML del proyecto. Flask utiliza esta carpeta para mostrar las páginas web.

---

### `templates/login.html`

Contiene la pantalla de inicio de sesión.

En esta página el usuario ingresa:

```txt
Usuario
Contraseña
```

Si los datos son correctos, el sistema permite ingresar al menú principal.

---

### `templates/menu.html`

Contiene el menú principal del sistema.

Desde esta página el usuario puede elegir entre:

```txt
Reglas del juego
Iniciar juego
Finalizar juego
```

---

### `templates/reglas.html`

Contiene la explicación de las reglas del juego.

Aquí se muestra qué opción gana contra cuál:

```txt
Piedra gana a tijera.
Papel gana a piedra.
Tijera gana a papel.
```

---

### `templates/juego.html`

Contiene la pantalla principal del juego.

En esta página el usuario puede seleccionar:

```txt
Piedra
Papel
Tijera
```

También muestra:

```txt
La jugada del usuario
La jugada de la computadora
El resultado de la ronda
El puntaje actual
```

---

### Carpeta `static/`

Esta carpeta contiene los archivos estáticos del proyecto, como CSS y JavaScript.

---

### `static/css/styles.css`

Contiene todos los estilos visuales del sistema.

Aquí se definen:

* Colores.
* Tamaños.
* Diseño de las tarjetas.
* Botones.
* Formularios.
* Mensajes de resultado.
* Estilos para victoria, derrota y empate.

---

### `static/js/script.js`

Contiene código JavaScript básico para apoyar la interfaz.

En este proyecto se usa de forma sencilla para comprobar que el archivo JavaScript se carga correctamente en la página del juego.

---

## Explicación del código de Python

El archivo principal del proyecto es `app.py`.

A continuación se explica cómo se utilizó Python en el programa.

---

## Importaciones principales

```python
from flask import Flask, render_template, request, redirect, url_for
import random
```

Estas líneas permiten importar herramientas necesarias para el proyecto.

### Flask

Flask se utiliza para crear la aplicación web.

```python
Flask
```

Permite iniciar el servidor.

```python
render_template
```

Permite mostrar archivos HTML.

```python
request
```

Permite recibir datos enviados desde formularios HTML.

```python
redirect
```

Permite redireccionar a otra página.

```python
url_for
```

Permite llamar rutas por su nombre.

### Random

```python
import random
```

Se utiliza para que la computadora pueda elegir aleatoriamente entre piedra, papel o tijera.

---

## Creación de la aplicación

```python
app = Flask(__name__)
```

Esta línea crea la aplicación Flask.

`__name__` es una variable especial de Python que indica el nombre del archivo que se está ejecutando.

---

## Variables de puntaje

```python
puntaje_usuario = 0
puntaje_computadora = 0
empates = 0
```

Estas variables almacenan los resultados del juego.

Aquí se aplican conceptos básicos de programación:

* Variables.
* Datos enteros.
* Almacenamiento de información.
* Actualización de valores.

Por ejemplo:

```python
puntaje_usuario = puntaje_usuario + 1
```

Esta línea suma un punto al usuario cuando gana una ronda.

---

## Función para obtener la jugada de la computadora

```python
def obtener_jugada_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)
```

Esta función permite que la computadora seleccione una opción al azar.

Aquí se utiliza una lista:

```python
opciones = ["piedra", "papel", "tijera"]
```

La lista almacena las tres opciones posibles del juego.

Luego se usa:

```python
random.choice(opciones)
```

Esto selecciona una opción aleatoria de la lista.

Esta parte representa el algoritmo que usa la computadora para jugar contra el usuario.

---

## Función para determinar el ganador

```python
def determinar_ganador(jugada_usuario, jugada_computadora):
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
```

Esta función contiene la lógica principal del juego.

Recibe dos parámetros:

```python
jugada_usuario
jugada_computadora
```

Luego compara ambas jugadas usando estructuras de decisión:

```python
if
elif
else
```

También utiliza operadores relacionales:

```python
==
```

Y operadores lógicos:

```python
and
```

La función analiza las reglas del juego:

```txt
Piedra gana contra tijera.
Papel gana contra piedra.
Tijera gana contra papel.
```

Si el usuario y la computadora eligen lo mismo, el resultado es empate.

Si el usuario cumple una de las condiciones ganadoras, el resultado es "Ganaste".

Si no se cumple ninguna condición anterior, el resultado es "Perdiste".

---

## Ruta principal

```python
@app.route("/")
def inicio():
    return redirect(url_for("login"))
```

Esta ruta se ejecuta cuando el usuario entra a la página principal.

En lugar de mostrar contenido directamente, redirige al usuario a la página de login.

---

## Ruta del login

```python
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
```

Esta ruta controla el inicio de sesión.

Cuando el usuario entra por primera vez, se muestra el formulario.

Cuando el usuario envía el formulario, se reciben los datos:

```python
usuario = request.form["usuario"]
password = request.form["password"]
```

Luego se validan con una condición:

```python
if usuario == "admin" and password == "1234":
```

Si los datos son correctos, el usuario pasa al menú.

Si los datos son incorrectos, se muestra un mensaje de error.

Aquí se aplican dos caminos principales:

```txt
Camino 1: Login correcto → Menú principal
Camino 2: Login incorrecto → Mensaje de error
```

---

## Ruta del menú

```python
@app.route("/menu")
def menu():
    return render_template("menu.html")
```

Esta ruta muestra el menú principal del juego.

Desde aquí el usuario puede ir a reglas, iniciar juego o finalizar.

---

## Ruta de reglas

```python
@app.route("/reglas")
def reglas():
    return render_template("reglas.html")
```

Esta ruta muestra la página donde se explican las reglas del juego.

---

## Ruta del juego

```python
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
```

Esta ruta maneja la pantalla del juego.

Primero se declaran variables vacías:

```python
jugada_usuario = ""
jugada_computadora = ""
resultado = ""
```

Cuando el usuario selecciona piedra, papel o tijera, se recibe el dato desde el formulario:

```python
jugada_usuario = request.form["jugada"]
```

Luego la computadora genera su jugada:

```python
jugada_computadora = obtener_jugada_computadora()
```

Después se determina el ganador:

```python
resultado = determinar_ganador(jugada_usuario, jugada_computadora)
```

Finalmente, se actualiza el puntaje dependiendo del resultado:

```python
if resultado == "Ganaste":
    puntaje_usuario = puntaje_usuario + 1

elif resultado == "Perdiste":
    puntaje_computadora = puntaje_computadora + 1

else:
    empates = empates + 1
```

Esta parte utiliza estructuras condicionales y operadores para controlar el comportamiento del programa.

---

## Ruta para reiniciar puntaje

```python
@app.route("/reiniciar")
def reiniciar():
    global puntaje_usuario, puntaje_computadora, empates

    puntaje_usuario = 0
    puntaje_computadora = 0
    empates = 0

    return redirect(url_for("juego"))
```

Esta ruta permite reiniciar el marcador.

Cuando el usuario presiona el botón de reiniciar, las variables vuelven a cero.

---

## Ejecución del programa

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Esta parte permite ejecutar el servidor Flask.

`debug=True` sirve para que Flask actualice automáticamente los cambios mientras se desarrolla el proyecto.

---

## Aplicación de los temas de programación

Este proyecto aplica los siguientes temas vistos en clase.

---

### Tema 1: Resolución de problemas

El problema consiste en crear un juego interactivo que permita al usuario jugar Piedra, Papel o Tijera contra la computadora.

La solución se divide en pasos:

```txt
1. Iniciar sesión.
2. Mostrar un menú.
3. Consultar reglas.
4. Iniciar una partida.
5. Elegir una jugada.
6. Generar una jugada para la computadora.
7. Comparar resultados.
8. Mostrar el ganador.
9. Actualizar el puntaje.
```

---

### Tema 2: Entorno de programación

El entorno utilizado fue:

```txt
Python 3.13
Flask
Visual Studio Code
HTML
CSS
JavaScript
Git
GitHub
```

---

### Tema 3: Manejo de datos

En el proyecto se usan diferentes tipos de datos.

### String

```python
usuario = "admin"
password = "1234"
resultado = "Ganaste"
```

### Enteros

```python
puntaje_usuario = 0
puntaje_computadora = 0
empates = 0
```

### Booleanos

Aunque no se declara directamente una variable booleana principal, Flask trabaja con condiciones que producen valores verdaderos o falsos, por ejemplo:

```python
request.method == "POST"
```

Esta expresión puede ser verdadera o falsa.

### Listas

```python
opciones = ["piedra", "papel", "tijera"]
```

### Operadores

Se utilizan operadores de comparación:

```python
==
```

Y operadores lógicos:

```python
and
```

---

### Tema 4: Algoritmos y diagramas de flujo

El algoritmo principal del juego es:

```txt
Inicio
↓
Mostrar login
↓
Validar usuario y contraseña
↓
Si los datos son correctos, mostrar menú
↓
El usuario selecciona iniciar juego
↓
El usuario elige piedra, papel o tijera
↓
La computadora elige una opción aleatoria
↓
Se comparan las jugadas
↓
Se muestra el resultado
↓
Se actualiza el puntaje
↓
El usuario puede volver a jugar o regresar al menú
↓
Fin
```

---

### Tema 5: Lógica de programación

Se utilizan condicionales para validar el login y determinar el resultado del juego.

Ejemplo:

```python
if usuario == "admin" and password == "1234":
    return redirect(url_for("menu"))
else:
    mensaje_error = "Usuario o contraseña incorrectos"
```

También se usan condicionales para saber quién ganó:

```python
if jugada_usuario == jugada_computadora:
    return "Empate"
elif jugada_usuario == "piedra" and jugada_computadora == "tijera":
    return "Ganaste"
else:
    return "Perdiste"
```

---

### Tema 6: Bucles

En este proyecto el uso de bucles se puede evidenciar principalmente en la lógica general del juego, porque el usuario puede jugar varias rondas sin cerrar el programa.

Aunque el ciclo no está escrito como un `while` tradicional en consola, el sistema web permite repetir el proceso cada vez que el usuario presiona una opción del juego.

La repetición ocurre de esta forma:

```txt
Elegir jugada
↓
Mostrar resultado
↓
Elegir otra jugada
↓
Mostrar nuevo resultado
```

También se puede utilizar un bucle `for` para recorrer las opciones del juego en una versión más básica de consola.

Ejemplo conceptual:

```python
opciones = ["piedra", "papel", "tijera"]

for opcion in opciones:
    print(opcion)
```

---

### Tema 7: Estructuras de datos y funciones

Se usan listas y funciones.

### Lista

```python
opciones = ["piedra", "papel", "tijera"]
```

La lista almacena las opciones disponibles para la computadora.

### Funciones

```python
def obtener_jugada_computadora():
```

Esta función genera la jugada de la computadora.

```python
def determinar_ganador(jugada_usuario, jugada_computadora):
```

Esta función determina el resultado de la partida.

Las funciones ayudan a dividir el programa en partes más pequeñas y fáciles de entender.

---

## Cómo ejecutar el proyecto

### 1. Clonar o descargar el proyecto

Si el proyecto está en GitHub, se puede clonar con:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego entrar a la carpeta:

```bash
cd piedra-papel-tijera-python
```

---

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar el entorno virtual

En Windows con Git Bash:

```bash
source venv/Scripts/activate
```

En Windows con PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar el proyecto

```bash
python app.py
```

---

### 6. Abrir el navegador

Ingresar a la siguiente dirección:

```txt
http://127.0.0.1:5000
```

---

## Credenciales de acceso

Para ingresar al sistema se usan las siguientes credenciales:

```txt
Usuario: admin
Contraseña: 1234
```

---

## Flujo principal del programa

```txt
Inicio
↓
Login
↓
¿Datos correctos?
├── No → Mostrar error
└── Sí → Menú principal
        ↓
        1. Ver reglas
        2. Iniciar juego
        3. Finalizar juego
```

---

## Flujo del juego

```txt
Inicio del juego
↓
Usuario elige piedra, papel o tijera
↓
Computadora elige una opción aleatoria
↓
Se comparan las jugadas
↓
¿Quién gana?
├── Usuario gana → Se suma punto al usuario
├── Computadora gana → Se suma punto a la computadora
└── Empate → Se suma empate
↓
Mostrar resultado
↓
Volver a jugar o regresar al menú
```

---

## Conclusión

Este proyecto permite practicar conceptos básicos de programación mediante el desarrollo de un juego sencillo e interactivo.

La lógica principal se encuentra en Python, donde se utilizan variables, tipos de datos, listas, funciones, condicionales y operadores lógicos. La interfaz gráfica se realiza con HTML, CSS y JavaScript, mientras que Flask permite conectar el backend con las páginas web.

El proyecto cumple con una estructura básica y comprensible, adecuada para un estudiante que está iniciando en programación.

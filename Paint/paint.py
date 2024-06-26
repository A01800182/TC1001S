"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

# Se import la libreria turtle
from turtle import *

# Se importa vector de freegames
from freegames import vector


# Esta funcion permite dibujar la linea trazada por el usuario
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Esta función permite que, dado los dos extremos inferiores de un cubo, el programa termina de dibujar la figura y la rellena 
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circulo(start, end):
    """Draw circle from start to end."""
    # Calculamos el radio del circulo a trazar
    radius = (((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5) / 2

    # Movemos el cursor al inicio de la trayectoria
    goto(start.x, start.y)
    down()

    # Movemos la disposicion de tal manera que el circulo se genere alrededor del radio
    forward(radius)
    setheading(270)
    forward(radius)
    setheading(0)

    # Rellenamos el circulo que se dibujara
    begin_fill()
    circle(radius)
    end_fill()

# Esta funcion traza un rectangulo y rellena su figura
def rectangle(start, end):
    up()
    # Calculamos el tamano de base del rectangulo, calculando la distancia entre los puntos seleccionados por el usuario
    base = (((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5)
    goto(start.x, start.y)
    down()
    # Comenzamos a rellenar la figura que trazaremos (el rectangulo)
    begin_fill()
    # Procedemos a avanzar el largo de la base, giramos 90 grados hacia la izquierda, y avanzamos el largo de la altura
    forward(base)
    left(90)
    forward(8)
    left(90)
    forward (base)
    left (90)
    forward(8)
    left(90)
    end_fill()

# Esta funcion traza un triangula y rellena su figura
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    # Calculamos el tamano de los lados del triangulo, calculando la distancia entre los puntos seleccionados por el usuario
    lado = (((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5) 
    goto(start.x, start.y)
    down()
    # Comenzamos a rellenar la figura que trazaremos (el triangulo)
    begin_fill()
    for _ in range(3):
        # Avanzamos la distancia calculada como el lado de la figura
        forward(lado)
        # Nos movemos hacia la izquierda en un angulo de 120 porque un triangulo tiene una suma total de angulos de 360 grados 
        left(120)
    end_fill()

# Con esta funcion, guardamos la posición de inicio de la figura y establecemos que el tipo de figura es la de 'linea'
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


# Esta función nos  permite cambiar los valores del diccionario 'state', el cual guarda los valores de posicion inicial y tipo de figura
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Inicializamos el diccionaro 'state', el cual guarda los valores de posicion inicial y tipo de figura
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Estas funciones lambda nos permiten cambiar el color de la figura
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# Añadimos un nuevo color por escoger
onkey(lambda: color('yellow'), 'Y')

# Estas funciones lambda nos permiten cambiar el tipo de figura
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
# Fin del programa 

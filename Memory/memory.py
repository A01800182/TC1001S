"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

# Importamos toda la funcionalidad de las librerias random y turtle, respectivamente
from random import *
from turtle import *

# Importamos path de freegames
from freegames import path

# Creamos las variables que guardaran la cantidad de intentos y de fichas volteadas correctamente
intentos = 0
fichasVolteadas = 0

# Tambien, creamos una variable para modificar el marcador
writer = Turtle(visible = False)

# Guardamos la imagen que se desplegara si el usuario termina el juego
car = path('car.gif')
# Creamos la lista de fichas en el tablero, la cual está compuesta por las letras de la A a la Z y unos simbolos, repetidos dos veces
tiles = [chr(65+i) for i in range(32)] * 2

# Guardamos en un diccionario el valor de la tarjeta que esté volteada
state = {'mark': None}
# Asignamos a todas las fichas del tablero como ocultas (volteadas)
hide = [True] * 64

# Esta funcion dibuja el tablero
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Esta funcion retorna el indice de una ficha del tablero, dada una coordenada xy
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Esta funcion realiza lo contrario que la anterior, ya que retorna una coordenada xy, dado el indice de una ficha del tablero
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Esta funcion nos permite manipular las consecuencias de los eventos del juego de memoria
def tap(x, y):
    global intentos, fichasVolteadas
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    # Aumentamos la cantidad de intentos realizados
    intentos += 1
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
	# Accion a seguir si es el primer turno del juego, si el jugador escogio la misma fecha, o si la que escogio no es la dupla de la ficha actual
        state['mark'] = spot
    else:
	# Accion a seguir si el jugador escoge la ficha que es la dupla de la ficha anteriormente seleccionada. Si esto se cumple, las fichas ya no se ocultan
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
	    # Aumentamos la cantidad de fichas correctamente seleccionadas
        fichasVolteadas += 2
	# Modificamos el marcador
    writer.undo()
    writer.write('Intentos: ' + str(intentos) + "\nFichas Volteadas: " + str(fichasVolteadas))
    if fichasVolteadas == 64:
        writer.undo()
        writer.write('Intentos: ' + str(intentos) + "\nFichas Volteadas: " + str(fichasVolteadas) + "\n¡Felicidades has destapado todos los cuadros!")

# Esta funcion se encarga de desplegar el tablero
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark],align="center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

# Esta funcion desordena las fichas
shuffle(tiles)

# A continuacion se establecen los parametros de la pantalla, del clic y de los graficos de turtle
setup(800, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)

# Desplegamos las estadisticas
writer.goto(225, 160)
writer.color('black')
writer.write('Intentos: ' + str(intentos) + "\nFichas Volteadas: " + str(fichasVolteadas))

# Seguidamente, se comienza el juego
draw()
done()

"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

# Añade las librerias necesarias para el correcto funcionamiento del juego
from random import randrange
from turtle import *

from freegames import vector

# Declara las variables de antemano
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Define la funcion "tap" para cuando reciba un click dispare la bola de canon
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Se agrego un multiplicador * 2 para duplicar la velocidad de la bola
        speed.x = ((x + 200) / 25) * 2
        speed.y = ((y + 200) / 25) * 2

# Define la funcion "inside" que detecta cuando deja la pantalla
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Define la funcion "draw" que dibuja la bola y los objetivos
def draw():
    """Draw ball and targets."""
    clear()

    # Mueve el cursor para dibujar los objetivos y los define como azules
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Define la posicion del cursor y define que la bola es roja
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Define la funcion "move" donde mueve los objetivos y la bola a una velocidad determinada
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Se multiplica por el factor de aceleracion que busco implementar a los targets
        target.x -= 0.5 * 1.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

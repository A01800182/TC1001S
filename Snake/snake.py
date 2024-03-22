"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

# Aqui hace los imports necesarios de las librerias par que funcione el codigo
from random import randrange
# Importamos de random choice para el movimiento de la comida
from random import choice
from turtle import *

from freegames import square, vector

# Declara las variables de antemano
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Define la funcion de cambio de direccion  de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

# Define la funcion "inside" que retorna un verdadero si la cabeza esta dentro del rango
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Agregamos la funcion de movimiento al azar de la comida
def moveFood():
    # Direcciones de movimiento, el vector zeros, es sin movimiento
    direcciones = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10), vector(0,0)]
    move = choice(direcciones)
    nextPosition = food + move

    if inside(nextPosition): # Verificamos que este dentro de los limites la nueva posicion
        food.move(move)
    else:
        moveFood() # Aqui usamos el metodo recursimo de una funcion (gracias profe -Juan)

# Define la funcion "move" que indica  la direccion a la que se movera
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    # Implementacion del Feature de movimiento de la comida
    moveFood()

    # Aqui define que pasa si choca consigo misma, se pone en rojo
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Define el if si come el puntito, crece un cuadrado
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Define el color del cuerpo de la serpiente y el de la comida
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

# Define los valores iniciales y los de cambio de moviento con las flechas
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

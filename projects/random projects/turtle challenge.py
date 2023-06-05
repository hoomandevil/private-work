import turtle
import random

tommy = turtle.Turtle()
screen = turtle.Screen()
tommy.shape("turtle")
tommy.speed(2)
turtle.colormode(255)

def random_colour( ):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

n = 3
for i in range(5):
    for _ in range(n):
        tommy.forward(60)
        tommy.right(360 / n)
    tommy.color("Red")
    n += 1

screen.exitonclick()


import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(20)
    tim.setheading(random.choice([0,90,180,270]))

screen.listen()
screen.onkey(key = "space", fun = move_forward)

screen.exitonclick()
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

#creating function for movements
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

#creating function for changing direction
def change_to_right():
    tim_heading = tim.heading() -10
    tim.setheading(tim_heading)
    # tim.right(10)


def change_to_left():
    tim_heading = tim.heading() + 10
    tim.setheading(tim_heading)
    # tim.left(10)

#defining a function for clearing the screen

def clear_screen():
    screen.resetscreen()


#creating event listeners
screen.listen()
screen.onkey(key="w", fun = move_forward)
screen.onkey(key="s", fun = move_backward)
screen.onkey(key="a", fun = change_to_left)
screen.onkey(key="d", fun = change_to_right)
screen.onkey(key= "c", fun = clear_screen)

screen.exitonclick()
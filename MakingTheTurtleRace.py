from turtle import Turtle, Screen
import random
#setting up screen
screen = Screen()
screen.setup(height=400,width=500)
user_guess = screen.textinput(title="Make A Bet", prompt="Guess the wining color, for a chance to double you money: ")
screen.title("You Guessed: " + user_guess)

colors = ["red", "orange", "gold","green", "blue", "purple"]
y = 150
turtles = []

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-230, y)
    new_turtle.pendown()
    y -= 50
    turtles.append(new_turtle)

if user_guess in colors:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        x_cordinate = turtle.xcor()
        if x_cordinate >= 250:
            game_is_on = False
            winner_color = turtle.pencolor()
            if user_guess == winner_color:
                print("You Won")
            else:
                print("You Lost")
            print(winner_color +" won the race.")

        random_distance = random.randint(1,10)
        turtle.forward(random_distance)












screen.exitonclick()
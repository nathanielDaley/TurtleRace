import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

TURTLE_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
TURTLE_POSITIONS = [-125, -75, -25, 25, 75, 125]
all_turtles = []

finish_line = Turtle()
finish_line.speed("fastest")
finish_line.penup()
finish_line.setposition(230, 170)
finish_line.setheading(270)
finish_line.pendown()
finish_line.forward(340)
finish_line.penup()
finish_line.forward(40)

for x in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(TURTLE_COLORS[x])
    new_turtle.goto(x=-230, y=TURTLE_POSITIONS[x])
    all_turtles.append(new_turtle)

winning_color = ""
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.pos()[0] > 220:
            winning_color = turtle.pencolor()
            is_race_on = False

for turtle in all_turtles:
    turtle.forward(10)
for turtle in all_turtles:
    turtle.forward(10)

if winning_color == user_bet:
    print("You were correct! You win!")
else:
    print(f"You were wrong! The winner was {winning_color}!")

screen.exitonclick()
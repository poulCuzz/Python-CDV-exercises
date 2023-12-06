import turtle
from turtle import *

turtle.title("kwadrat")
turtle.shape("turtle")
myTurtle = Turtle()
myTurtle.pendown()
for x in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)


turtle.exitonclick()


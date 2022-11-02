
from random import randint
from turtle import *
import turtle

inflation_rate = 20
tracer(0,1)
for _ in range(20):
    inflation_rate +=  randint(-10, 40)
    while True:
        turtle.forward(2)
        turtle.left(90)

        turtle.forward(inflation_rate)
        turtle.left(90)

        turtle.forward(2)
        turtle.left(90)

        turtle.forward(inflation_rate)
        turtle.left(90)
        break
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    update()   
exitonclick()

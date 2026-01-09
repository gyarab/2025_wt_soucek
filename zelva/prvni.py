from turtle import forward, left, right, exitonclick
from math import sqrt

def house(a):
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    left(135)
    forward(a/(sqrt(2)))
    left(90)
    forward(a/(sqrt(2)))
    left(45)
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    left(90)

def planet(a):
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    left(135)
    forward(a/(sqrt(2)))
    left(90)
    forward(a/(sqrt(2)))
    left(45)
    forward(a)
    left(135)
    forward(sqrt(2*a**2))
    right(135)
    forward(a)
    left(45)

house(50)
planet(50)
house(50)


exitonclick()
from turtle import forward, left, right, exitonclick
from math import sqrt

b=sqrt(2*a**2)
c=a/(sqrt(2))

def house(a):
    forward(a)
    left(135)
    forward(b)
    right(135)
    forward(a)
    left(135)
    forward(c)
    left(90)
    forward(c)
    left(45)
    forward(a)
    left(135)
    forward(b)
    right(135)
    forward(a)
    left(90)

def planet(a):
    forward(a)
    left(135)
    forward(b)
    right(135)
    forward(a)
    left(135)
    forward(c)
    left(90)
    forward(c)
    left(45)
    forward(a)
    left(135)
    forward(b)
    right(135)
    forward(a)
    left(45)

house(50)
planet(50)
house(50)


exitonclick()
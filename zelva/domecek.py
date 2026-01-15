from turtle import forward, left, right, exitonclick
from math import sqrt
from random import randint

def house(a):
    b=sqrt(2*a**2)
    c=a/(sqrt(2))
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
    b=sqrt(2*a**2)
    c=a/(sqrt(2))
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

for _ in range(12):
    size = randint(20, 100)
    print("house size: ", size)

planet(size)
planet(size)
planet(size)
planet(size)

exitonclick()
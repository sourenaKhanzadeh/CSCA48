from turtle import *
from Compsci_II.Practices.sequences import *
import sys

sys.setrecursionlimit(99999)

mt = math()
screen = Screen()
t = Turtle()
t.speed(150)


# cool star
def x__I(n):

    t.left(n)
    t.forward(n-1)
    x__I(n+1)


# cool spiral
def x__II(n: int):
    t.left(2)
    t.forward(n/2)
    t.right(90)
    x__II(n+1)


# cool square
def x__III(n):
    t.left(90)
    t.forward(n**(12/13))
    x__III(n+1)


# cool shape in the center
def x__IV(n:int):
    t.left(n/2)
    t.forward(n**2)
    t.home()
    x__IV(n+1)


# makes a trapezoid
# then its infinite symmetry
def x__V(n: int):
    t.backward(n)
    t.right(45)
    t.forward(n)
    t.left(45)
    t.forward(n)
    t.left(45)
    t.forward(n)
    t.home()
    x__V(n+1)
    # t.home()


x__V(-300)

screen.exitonclick()

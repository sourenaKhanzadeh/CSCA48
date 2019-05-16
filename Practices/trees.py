# Recursive Tree Challenge - www.101computing.net/recursive-tree-challenge
from turtle import *
from random import randint

t = Turtle()
s = Screen()

# Recursive function to draw a tree, branch by branch


def drawTree(level, size, angle, ratio):
    if level >= 0:
        t.forward(size)
        t.left(angle)
        drawTree(level - 1, size / ratio, angle, ratio)
        t.right(2 * angle)
        # Draw right branch of the tree
        drawTree(level - 1, size / ratio, angle, ratio)
        t.left(angle)
        t.forward(-size)
    else:
        # Stop the recursion
        return


# Main Program Starts Here
t.speed(0)
t.penup()
t.goto(0, -180)
t.left(90)
t.pendown()

# Draw a tree using a recursive function
size = randint(80, 120)
angle = randint(20, 40)
ratio = randint(14, 18) / 10
level = randint(8, 10)

drawTree(level, size, angle, ratio)
s.exitonclick()

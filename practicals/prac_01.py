import turtle

x = turtle.Turtle()
wn = turtle.Screen()

z = []


def rec(n):
    x.speed(100)
    if n == 0:
        x.forward(1)
    else:
        x.forward(n)
        x.left(45)
        rec((n-.9999999999999))

for i in range(12):
    z.append(i)
    y = sum(z)
    z.pop()
rec(y)
wn.exitonclick()

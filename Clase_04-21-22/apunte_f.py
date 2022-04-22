from turtle import *
from time import *

showturtle()
shape('turtle')
backward(15)
forward(15)
goto(10, 10)
home()
left(90)
right(90)
setheading(90)

reset()
colormode(255)
pencolor((255, 0, 0))
for i in range(25):
    forward(10*i)
    left(90)

reset()
colormode(255)
pencolor((0, 100, 0))
for i in range(25):
    forward(10*i)
    left(90)

reset()


def main():
    setup(500, 400, 50, 50)
    done()


main()

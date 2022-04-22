### Ajedrez
from turtle import *


def main():
    configuraVentana()
    imprimeTablero()


def configuraVentana():
    st()
    penup()
    setpos(-200, -200)
    pendown()
    speed(0)


def imprimeTablero():
    d = 0
    for c in range(4):
        d += 1
        if (c != 0):
            ht()
            penup()
            setpos(-200, -200+(50*(d)))
            pendown()
            st()
        for b in range(4):
            begin_fill()
            for a in range(4):
                forward(50)
                right(90)
            end_fill()
            forward(50)
            for a in range(4):
                forward(50)
                right(90)
            forward(50)
        ht()
        penup()
        if d > 1:
            d += 1
        setpos(-200, -200+(50*(d)))
        pendown()
        st()
        for b in range(4):

            for a in range(4):
                forward(50)
                right(90)

            forward(50)
            begin_fill()
            for a in range(4):
                forward(50)
                right(90)
            end_fill()
            forward(50)

    ht()
    done()


main()

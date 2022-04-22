### Panda

from turtle import *


def main():
    configuraVentana()
    dibujaOrejas()
    dibujaContornoCara()
    dibujaOjos()
    dibujaNariz()
    dibujaBoca()
    done()


def configuraVentana():
    setup(1280, 720)
    title("Panda")
    st()
    penup()
    setpos(-200, 200)
    pendown()
    speed(0)


def dibujaOrejas():
    begin_fill()
    circle(75)
    end_fill()
    penup()
    setpos(200, 200)
    pendown()
    begin_fill()
    circle(75)
    end_fill()


def dibujaContornoCara():
    color('black', 'white')
    penup()
    setpos(0, -50)
    pendown()
    begin_fill()
    circle(200)
    end_fill()


def dibujaOjos():
    color('black')
    penup()
    setpos(-100, 150)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
    penup()
    setpos(100, 150)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
    ###
    color('white')
    penup()
    setpos(-100, 165)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    setpos(100, 165)
    pendown()
    begin_fill()
    circle(20)
    end_fill()


def dibujaNariz():
    color('black')
    penup()
    setpos(0, 75)
    pendown()
    begin_fill()
    circle(40)
    end_fill()


def dibujaBoca():
    color('black')
    right(50)
    pensize(5)
    circle(30, 180)
    penup()
    setpos(0, 75)
    pendown()
    color('black')
    left(360)
    pensize(5)
    circle(30, 180)
    penup()


main()

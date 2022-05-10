import turtle
import time


def main():
    run = True
    turtle.st()
    turtle.left(90)
    turtle.forward(150)
    numero = -1
    while run:
        turtle.clear()
        numero += 1
        turtle.write(f"Hola Mundo {numero}", False, align="center")

        time.sleep(0.1667)


main()

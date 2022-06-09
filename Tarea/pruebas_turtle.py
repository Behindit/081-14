import turtle
import time



def main():
    def movimiento():
        y=recblanc.ycor()
        y+=90
        recblanc.sety(y)

    ###### Configuracion pantalla
    Ventana=turtle.Screen()
    Ventana.title("Pong")
    Ventana.bgcolor("green")
    Ventana.setup(width=900,height=450)

    ##### tortuga

    recblanc= turtle.Turtle()
    recblanc.shape("square")
    # recblanc.shapesize(stretch_len=2, stretch_wid =25)

    ##### movimiento

    Ventana.listen()
    Ventana.onkeypress(movimiento,"w")
    turtle.done()

main()

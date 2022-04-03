def main():
    hora = leeHora("Ingrese hora: ")
    minutos = leeMinutos("Ingrese minutos: ")
    calculaVagones(hora, minutos)


def leeHora(texto):
    ingreso_hora = int(input(texto))

    while ingreso_hora > 23 or ingreso_hora < 0:

        ingreso_hora = int(
                input("Solo puede ingresar valores entre las 00 y 23 horas: "))

    return ingreso_hora


def leeMinutos(texto2):
    ingreso_minutos = int(input(texto2))

    while ingreso_minutos < 0 or ingreso_minutos > 59:
        ingreso_minutos = int(
            input("Solo puede ingresar valores entre 0 y 59 minutos: "))
    return ingreso_minutos


def horario(hora, minutos):
    if hora < 6 or hora > 22:
        print("Ya no se encuentran trenes en este horario")
        horario_vagon = "fuera"

    else:

        if (hora >= 7 and minutos >= 30) and (hora == 9 and minutos == 0):
            print("Se encuentra en horario punta")
            horario_vagon = "punta"
        else:
            if (hora > 7 or (hora == 7 and minutos >= 30)) and (hora < 9):
                print("Se encuentra en horario punta")
                horario_vagon = "punta"
            else:
                if ((hora >= 18 and minutos >= 0) and (hora == 19 and minutos == 0)):
                    print("Se encuentra en horario punta")
                    horario_vagon = "punta"
                else:
                    if ((hora >= 18 and minutos >= 0) and (hora < 19 and minutos >= 0)):
                        print("Se encuentra en horario punta")
                        horario_vagon = "punta"
                    else:
                        if (hora >= 6 and minutos >= 00) and (hora < 23):
                            print("Se encuentra en horario normal")
                            horario_vagon = "normal"

    return horario_vagon


def calculaVagones(hora, minutos):

    horario_vagon = horario(hora, minutos)

    if horario_vagon == "normal":

        if (minutos % 12 == 0):
            print("El tren tiene 4 vagones")
            print("El tren se encuentra en el anden!!")
        else:
            print("El tren tiene 4 vagones")
            print("Debe esperar: ", 12-(minutos % 12), " Minutos")

    else:
        if horario_vagon != "fuera":

            if (minutos % 6 == 0):
                if ((minutos % 6 == 0) and (minutos % 12 != 0)):
                    print("El tren tiene 2 vagones")

                else:
                    print("el tren tiene 4 vagones")
                    print("El tren se encuentra en el anden!!")

            else:
                if ((minutos % 6 == 0) and (minutos % 12 != 0)):
                    print("El tren tiene 2 vagones")

                else:
                    print("el tren tiene 4 vagones")
                    print("Debe esperar: ", 6-(minutos % 6), " Minutos")


main()

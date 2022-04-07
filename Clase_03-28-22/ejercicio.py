def main():
    euros = leeEuros()
    (e500, e200, e100, e50, e20, e10, e5, e2, e1) = desglosaEuros(euros)
    despliegueFinal(e500, e200, e100, e50, e20, e10, e5, e2, e1)


def leeEuros():
    ingreso = int(input("Ingrese la cantidad de euros(1-1000): "))

    while (ingreso < 1 or ingreso > 1000):
        if ingreso < 1:
            print("Ingreso un valor menor a 1!")
            ingreso = input("Ingrese la cantidad de euros(1-1000): ")
        else:
            if ingreso > 1000:
                print("Ingreso un valor mayor a 1000!")
                ingreso = input("Ingrese la cantidad de euros(1-1000): ")

    return ingreso


def desglosaEuros(euros):

    if (euros//500) > 0:
        e500 = euros//500
        euros -= 500*e500
    else:
        e500 = 0

    if (euros//200) > 0:
        e200 = euros//200
        euros -= 200*e200
    else:
        e200 = 0

    if (euros//100) > 0:
        e100 = euros//100
        euros -= 100*e100
    else:
        e100 = 0

    if (euros//50) > 0:
        e50 = euros//50
        euros -= 50*e50
    else:
        e50 = 0

    if (euros//20) > 0:
        e20 = euros//20
        euros -= 20*e20
    else:
        e20 = 0

    if (euros//10) > 0:
        e10 = euros//10
        euros -= 10*e10
    else:
        e10 = 0

    if (euros//5) > 0:
        e5 = euros//5
        euros -= 5*e5
    else:
        e5 = 0

    if (euros//2) > 0:
        e2 = euros//2
        euros -= 2*e2
    else:
        e2 = 0

    if (euros//1) > 0:
        e1 = euros//1
        euros -= 1*e1
    else:
        e1 = 0

    return e500, e200, e100, e50, e20, e10, e5, e2, e1


def despliegueFinal(e500, e200, e100, e50, e20, e10, e5, e2, e1):

    if e500 > 0:
        print("Billetes de 500€: ", e500)
    if e200 > 0:
        print("Billetes de 200€: ", e200)
    if e100 > 0:
        print("Billetes de 100€: ", e100)
    if e50 > 0:
        print("Billetes de 50€: ", e50)
    if e20 > 0:
        print("Billetes de 20€: ", e20)
    if e10 > 0:
        print("Billetes de 10€: ", e10)
    if e5 > 0:
        print("Billetes de 5€: ", e5)
    if e2 > 0:
        print("Monedas de 2€: ", e2)
    if e1 > 0:
        print("Monedas de 1€: ", e1)

    suma_billetes = e500+e200+e100+e50+e20+e10+e5
    suma_monedas = e2+e1

    if suma_billetes > 0:

        ########################################

        if suma_billetes == 1 and suma_monedas == 0:
            print("Dando un total de ", suma_billetes, " billete.")
        if suma_billetes == 1 and suma_monedas > 0:
            print("Dando un total de ", suma_billetes, " billete", end=(""))
        if suma_billetes > 1 and suma_monedas == 0:
            print("Dando un total de ", suma_billetes, " billetes.")
        if suma_billetes > 1 and suma_monedas > 0:
            print("Dando un total de ", suma_billetes, " billetes", end=(""))

        ########################################

    if suma_monedas > 0:

        if suma_monedas == 1 and suma_billetes <= 0:
            print("Dando un total de ", suma_monedas, " moneda.")
        if suma_monedas > 1 and suma_billetes <= 0:
            print("Dando un total de ", suma_monedas, " monedas.")
        elif suma_monedas == 1:
            print(" y ", suma_monedas, " moneda.")
        elif suma_monedas > 0:
            print(" y ", suma_monedas, " monedas.")


main()

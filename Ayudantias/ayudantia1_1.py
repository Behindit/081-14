from random import randint


def main():
    inicial = leeNumeroInicial("Ingresa rango inicial: ")
    final = leeNumeroFinal("Ingresa rango final: ", inicial)
    numero = generaNumero(inicial, final)
    muyFrio, frio, tibio, caliente, muyCaliente, encontrado = buscaNumero(
        numero)
    imprimeResultado(muyFrio, frio, tibio, caliente, muyCaliente, encontrado)


def leeNumeroInicial(texto):

    numeroIngresado = int(input(texto))

    return numeroIngresado


def leeNumeroFinal(texto, inicial):

    numeroIngresado = int(input(texto))

    while ((numeroIngresado-inicial) < 30):

        numeroIngresado = int(input(texto))

    return numeroIngresado


def generaNumero(inicial, final):

    numeroGenerado = randint(inicial, final)

    return numeroGenerado


def buscaNumero(numero):

    muyFrio, frio, tibio, caliente, muyCaliente, encontrado = 0, 0, 0, 0, 0, 0

    numeroAdivinado = int(input("Ingresa numero: "))

    while numeroAdivinado != numero:

        if numeroAdivinado > numero:
            resta = numeroAdivinado-numero
        else:
            resta = numero-numeroAdivinado

        if ((resta <= 5) and (resta >= 1)):
            muyCaliente += 1
            print("Muy caliente")

        else:
            if ((resta <= 10) and (resta > 5)):
                caliente += 1
                print("Caliente")

            else:
                if ((resta <= 15) and (resta > 10)):
                    tibio += 1
                    print("Tibio")
                else:
                    if ((resta <= 25) and (resta > 15)):
                        frio += 1
                        print("Frio")
                    else:
                        if (resta > 25):
                            muyFrio += 1
                            print("Muy frio")

        numeroAdivinado = int(input("Ingresa numero: "))
    return muyFrio, frio, tibio, caliente, muyCaliente, encontrado


def imprimeResultado(muyFrio, frio, tibio, caliente, muyCaliente, encontrado):

    print(f"Muy Frio {muyFrio} Veces")
    print(f" Frio {frio} Veces")
    print(f"Tibio {tibio} Veces")
    print(f"Caliente {caliente} Veces")
    print(f"Muy Caliente {muyCaliente} Veces")

    sumaEquivocaciones = muyFrio+frio+tibio+caliente+muyCaliente

    print(
        f"¡¡Tuviste {sumaEquivocaciones} intentos incorrectos antes de encontrar la solucion")


main()

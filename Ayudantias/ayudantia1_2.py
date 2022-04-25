def main():
    cant = leeNumero("Numero de universidades: ")
    univ_A, univ_R, univ_E = cuentaVotos(cant)
    imprimeVotos(univ_A, univ_R, univ_E)


def leeNumero(texto):

    cantidadUni = int(input(texto))

    while (cantidadUni <= 0):

        cantidadUni = int(input(texto))


def cuentaVotos(cantidad):

    for a in range(cantidad):

        nombreUni = input("Universidad: ")
        print("Su voto debe ser: A=Aceptar // R=Rechazar // N=Nulo // B=Blanco")

        while voto != X:

            voto = input("Voto: ")

            voto.upper()

            if voto == "A":

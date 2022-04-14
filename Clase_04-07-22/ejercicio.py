
def main():
    numfrase = leeNumeroFrases()
    procesaFrase(numfrase)


def leeNumeroFrases():

    numero = int(input("¿Cuantas frases?(>2): "))

    while numero < 2 or numero == "":

        numero = int(input("Ud, ingresó {numero}, no es valido!!"))

    return numero


def procesaFrase(numeroFrases):

    frase = input("Ingrese Frase no vacia: ")
    while frase == "":
        print("No ingreso una frase!!")
        frase = input("Ingrese Frase no vacia: ")

    fraseGrande = len(frase)
    caracteresfrase = frase

    for i in range(numeroFrases-1):
        frase = input("Ingrese Frase no vacia: ")

        while frase == "":
            print("No ingreso una frase!!")
            frase = input("Ingrese Frase no vacia: ")

        if len(frase) > fraseGrande:
            fraseGrande = len(frase)
            caracteresfrase = frase

    print("Frase mas larga", caracteresfrase)


main()

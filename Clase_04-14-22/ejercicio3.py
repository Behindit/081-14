from random import *


def main():
    letras = "ABCDE"
    largo = leeNumero()
    secuencia = creaSecuencia(letras, largo)
    imprimeSecuencia(secuencia)


def leeNumero():
    largo_secuencia = int(input("Largo de la secuencia: "))

    while not largo_secuencia.isdigit():
        largo_secuencia = int(input("Largo de la secuencia: "))


def creaSecuencia(letras, largo):

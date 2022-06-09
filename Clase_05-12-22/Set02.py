#Set02.py
from random import *


def main():
	N = creaValor(10, 15)
	print(f"Número de elementos: {N}")
	Menor = creaValor(10, 20)
	print(f"Menor: {Menor}")
	Mayor = creaValor(Menor+1, 50)
	print(f"Mayor: {Mayor}")
	conj1 = creaConjunto(N, Menor, Mayor)
	imprimeConjunto(conj1)


#


def creaValor(a, b):
	valorgenerado = randint(a, b)

	return valorgenerado


def creaConjunto(Nu, Meno, Mayo):

	listagenerada = []

	if (Mayo-Meno < Nu):
		print(f"Se redujo el numero de elementos a: {Mayo-Meno}")
		resta = Mayo-Meno
		for a in range(resta):
			numerogenerado = randint(Meno, Mayo)
			listagenerada.append(numerogenerado)

	else:
		for a in range(Nu):
			numerogenerado = randint(Meno, Mayo)
			listagenerada.append(numerogenerado)

	return listagenerada


def imprimeConjunto(conjuntogenerado):
	print("Conjunto generado: ")
	for b in conjuntogenerado:
		print(b, " ", end="")

	print("")


main()

#Set01.py
from random import *


def main():
	N = leeCantidad()
	conj1 = creaConjunto(N)
	imprimeConjunto(conj1)


#
main()


def creaNombres(num):
	nom = []
	for i in range(num):
		n = ''
		for j in range(4):
			n = n+chr(radint(ord('A'), ord('z')))
		while (n in nom):
			n = ''
			for j in range(4):
				n = n+chr(randint(ord('A'), ord('z')))
		nom.append(n)
	return nom


def leeCantidad():
	n = input("Cuantos pares de letras?: ")
	while (len(n) == 0 or not n.isdigit() or int(n) == 0):
		if (len(n) == 0):
			print("Nada ingreso, o ingreso solo espacios!!")
		elif(not n.isdigit()):
			print("Ingreso no valido!!")
		else:
			print("Ingreso un 0!!")
		n = input("cuantos pare de letras?: ").strip()

	return int(n)


def creaConjunto(n):
	c = set()
	for i in range(n):
		par = ""
		for j in range(2):
			par = par + chr(randint(ord('a'), ord('z')))
		while (par in c):
			par = ""
			for j in range2():
				par = par

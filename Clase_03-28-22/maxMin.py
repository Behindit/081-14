from random import *


def main():
    n = leeEntero()
    escribeResultados(n)


def leeEntero():
    ingreso = int(input("Ingrese un numero entero entre 2 y 20: "))

    while ingreso < 2 or ingreso > 20:
        if (ingreso < 2):
            ingreso = int(
                input(f"Ingreso {ingreso}, debe ingresar un numero mayor a 2: "))
        else:
            if (ingreso > 20):
                ingreso = int(
                    input(f"Ingreso {ingreso}, debe ingresar un numero menor a 20: "))

    return ingreso


def escribeResultados(n):
    print(f"Secuencia de {n} numeros aleatorios:")
    numero_aleatorio = randint(10, 50)
    print(numero_aleatorio, end=" ")
    numero_menor = numero_aleatorio
    numero_mayor = numero_aleatorio
    for i in range(n-1):
        numero_aleatorio = randint(10, 50)

        if (numero_aleatorio < numero_menor):
            numero_menor = numero_aleatorio

        if (numero_aleatorio > numero_mayor):
            numero_mayor = numero_aleatorio
        print(numero_aleatorio, end=" ")

    print("")
    print(f"El numero menor: {numero_menor}")
    print(f"El numero mayor: {numero_mayor}")


main()

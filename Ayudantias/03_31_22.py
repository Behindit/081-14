def main():
    cantidad_numeros = leeEntero("Ingrese cantidad de numeros perfectos: ")
    minimo_numero = leeMinimo("Ingrese primer numero del rango: ")
    imprimePerfectos(cantidad_numeros, minimo_numero)


def leeEntero(texto):
    cantidad = int(input(texto))

    while cantidad <= 0:
        if (cantidad < 0):
            cantidad = int(
                input("Ingreso un numero negativo! ingrese nuevamente: "))
        if (cantidad == 0):
            cantidad = int(
                input("Ingreso un numero negativo! ingrese nuevamente: "))

    return cantidad


def leeMinimo(texto2):
    minimo = int(input(texto2))

    while minimo < 10:
        minimo = int(
            input("Ingreso un numero menor a 10! ingrese nuevamente: "))

    return minimo


def imprimePerfectos(cantidad, minimo):

    print(f"{cantidad} numeros perfectos, comenzando con el {minimo}")
    contador = 0

    while contador < 3:

        suma = descomponerNumero(minimo)

        if suma == 18:
            contador += 1
            print(minimo, end=(" "))

        minimo += 1
    print()


def descomponerNumero(minimo):

    suma = 0

    while minimo > 0:
        digito = minimo % 10
        suma += digito
        minimo = int(minimo//10)

    return suma


main()

def main():
    num1 = leeEntero("Escriba el primer entero positivo: ")
    num2 = leeEntero("Escriba el segundo entero positivo: ")
    binum1, binum2 = imprimeRetornaBinarios(num1, num2)
    imprimeBitwise(num1, num2, binum1, binum2)


def leeEntero(Texto):
    Numero = int(input(Texto))
    while Numero <= 0:
        if Numero == 0:
            Numero = input(Texto)
        else:
            Numero = input(Texto)
    return Numero


def imprimeRetornaBinarios(numero1, numero2):
    num1, num2 = int(numero1), int(numero2)
    print("Primer entero: ", numero1, " - En binario: ", bin(numero1))
    print("Segundo entero: ", numero2, " - En binario: ", bin(numero2))
    binum1 = bin(num1)
    binum2 = bin(num2)
    return binum1, binum2


def imprimeBitwise(numero1, numero2, binum1, binum2):

    print("Bitwise AND en decimal: ", numero1 & numero2,
          " Y en binario: ", bin(numero1 & numero2))
    print("Bitwise OR en decimal: ", numero1 | numero2,
          " Y en binario: ", bin(numero1 | numero2))
    print("Bitwise XOR en decimal: ", numero1 ^ numero2,
          " Y en binario: ", bin(numero1 ^ numero2))
    print("Bitwise ~ en decimal: ", ~numero1,
          " Y en binario: ", bin(~numero1))
    print("Bitwise << en decimal: ", numero1 << 4,
          " Y en binario: ", bin(numero1 << 4))
    print("Bitwise >> en decimal: ", numero1 >> 4,
          " Y en binario: ", bin(numero1 >> 4))


main()

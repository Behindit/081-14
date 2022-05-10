def main():
    x = valor("Ingrese coordenada x del punto: ")
    # y = valor("Ingrese coordenada y del punto: ")
    # m = valor("Ingrese pendiente de la recta: ")
    # b = valor("Ingrese intercepto de la recta: ")
    # r = creaTupla("Tupla de la recta: ", m, b)
    # p = creaTupla("Tupla del punto: ", x, y)
    # validaPuntoEnRecta(p, r)


def valor(texto):
    valorIngresado = input(texto).strip()

    while (len(valorIngresado) or not valido(valorIngresado)):
        if (len(valorIngresado) == 0):
            print("Nada ingresó, o ingresó sólo espacios!!")
        else:
            print("Secuencia no válida!")
        valorIngresado = input(texto)
    return float(valorIngresado)


def valido(n):

    if(n.isdigit() and int(n) != 0):
        return True
    return False


main()

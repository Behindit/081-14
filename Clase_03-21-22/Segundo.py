def main():
    num1 = ingresentero(input("Ingrese un numero entero: "))
    num2 = ingresentero(input("Ingrese un numero entero: "))
    suma = operaEnteros(num1, num2, '+')
    multi = operaEnteros(num1, num2, '*')
    divnormal = operaEnteros(num1, num2, '/')
    diventero = operaEnteros(num1, num2, '//')
    resultados(num1, num2, suma, multi, divnormal, diventero)


def operaEnteros(Numero1, Numero2, Operador):
    if Operador == '+':
        Numero1 += Numero2
    elif Operador == '*':
        Numero1 *= Numero2
    elif Operador == '/':
        Numero1 /= Numero2
    else:
        Numero1 //= Numero2

    return Numero1


def ingresentero(Numero):
    Numero = int(Numero)
    while Numero <= 0:
        if Numero == 0:
            Numero = input("Ingreso 0, ingrese un numero entero positivo")
        else:
            Numero = input(
                "Ingreso un numero negativo, ingrese un numero entero positivo")
    return Numero


def resultados(Numero01, Numero02, suma, multi, divnormal, diventero):
    print("El primer numero es: ", Numero01)
    print("El Segundo numero es: ", Numero02)
    print("""El resultado de la suma entre el primero y el segundo con el operador += es: """, suma)
    print("""El resultado de la multiplicacion entre el primero y el segundo con el operador *= es:""", multi)
    print("""El resultado de la division entre el primero y el segundo con el operador /= es:""", divnormal)
    print("""El resultado de la division entera entre el primero y el segundo con el operador //= es:""", diventero)


main()

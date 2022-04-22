def main():
    c = cuentaFrases()
    imprimeCuenta(c)


def cuentaFrases():

    caracteres = 0
    sigue = True
    contador_frase = 0

    while sigue:

        fraseValidar = input("Ingrese frase valida: ")

        for i in fraseValidar:
            if i != " ":
                caracteres += 1

        if fraseValidar == "" and contador_frase == 0:
            print("Ingreso nada")
            fraseValidar = input("Ingrese frase valida")
        else:
            if caracteres == 0 and contador_frase == 0:
                print("Ingreso espacio vacios")
                fraseValidar = input("Ingrese frase valida")
            else:
                if caracteres == 0 or fraseValidar == "":
                    sigue = False
                else:
                    contador_frase += 1

    return contador_frase


def imprimeCuenta(c):

    if c == 1:
        print(f"Se ingreso solo {c} frase valida")

    else:
        if c == 0:
            print("No se ingreso frase alguna!!")
        else:
            print(f"Se ingresaron {c} frases validas")


main()

def main():
    frase = leeFraseValida()
    cuenta = cuentaPalabras(frase)
    resultadosCuenta(frase, cuenta)


def leeFraseValida():
    fraseValidar = input("Ingrese frase valida")
    caracteres = 0
    invalido = True

    while invalido:

        for i in fraseValidar:
            if i != " ":
                caracteres += 1

        if fraseValidar == "":
            print("Ingreso nada")
            fraseValidar = input("Ingrese frase valida")
        else:
            if caracteres == 0:
                print("Ingreso espacio vacios")
                fraseValidar = input("Ingrese frase valida")
            else:
                invalido = False

    return fraseValidar


def cuentaPalabras(frase2):
    caracteres = 0

    for a in frase2:
        if a == " ":

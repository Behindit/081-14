def main():
    frase = validaFrase()
    nfrase = eliminaBlancosExtremos(frase)
    print(nfrase)


def validaFrase():
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


def eliminaBlancosExtremos(f):

    nf = " "
    i = 0
    while(f[i] == " "):
        i += 1
    nf = f[i:]
    c = len(nf)
    j = c-1
    while (nf[j] == ""):
        j -= 1
    fin = nf[:j+1]
    print(
        f"La frase sin espacios en bordes contiene {len(fin)} caracteres y es: ")
    return fin


main()

def main():
    c1_1 = leeComplejo("Ingrese la parte real del primer numero: ")
    c1_2 = leeComplejo("Ingrese la parte imaginaria del primer numero: ")
    c2_1 = leeComplejo("Ingrese la parte real del segundo numero: ")
    c2_2 = leeComplejo("Ingrese la parte imaginaria del segundo numero: ")

    resultadosComplejos(c1_1, c1_2, c2_1, c2_2)


def leeComplejo(texto):
    numero = float(input(texto))

def resultadosComplejos(c1_1, c1_2, c2_1, c2_2):

    print("La suma de los 2 numeros complejos ingresados es: ")

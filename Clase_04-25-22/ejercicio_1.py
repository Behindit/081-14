from random import randint


def main():
    N = creaValor("Tamaño de la lista: ", 3, 19)
    L1 = creaLista(N)
    imprimeLista(L1)
    V = creaValor("Nuevo valor a agregar: ", 10, 50)
    L2 = insertaValor(V, L1)
    imprimeLista(L2)


def creaValor(texto, inicio, final):

    valorGenerado = randint(inicio, final)

    print(texto, valorGenerado)

    return valorGenerado


def creaLista(largo_lista):
    lista_hecha = []

    for a in range(largo_lista):
        b = randint(10, 50)
        lista_hecha.insert(b)

    return lista_hecha

def

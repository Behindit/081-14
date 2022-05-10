def main():
    cursos = ["Algebra", "Geometria", "Calculo", "Programacion"]
    for a in cursos:
        print(f"{a} ", end="")
    print()


def segunda():

    cursos = ["Algebra", "Geometria", "Calculo", "Programacion"]
    print(*cursos, sep=(" "))


def unirse():

    cursos = ["Algebra", "Geometria", "Calculo", "Programacion"]
    print(" ".join(cursos))


def notass():
    notas_cursos = [4.5, 5.9, 6.4, 6.0]
    print(" ".join(map(str, notas_cursos)))


def asignacion_notas():
    notas_cursos = [4.5, 5.9, 6.4, 6.0]
    Algebra, Geometria, Calculo, Programacion = notas_cursos
    print(f"Notas de Algebra: {Algebra}")
    print(f"Notas de Calculo: {Calculo}")
    print(f"Notas de Programacion: {Programacion}")
    print(f"Notas de Geometria: {Geometria}")


def listas_numericas():

    uno = [1, 3, 5, 7]
    dos = list(uno)
    tres = list(range(1, 8, 2))
    print("uno= ", *uno, sep=" ")
    print("dos= ", *dos, sep=" ")
    print("tres= ", *tres, sep=" ")


def nombres():

    nombres1 = ["Alan", "Nicolas", "Daniel"]

    A = nombres1

    print(id(nombres1) == id(A))

    B = nombres1[:]

    print(id(nombres1) == id(B))


nombres()

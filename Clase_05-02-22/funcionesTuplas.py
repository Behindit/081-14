def primero():
    print(all([2, 3, 4]))
    print(all([1, 0, 2]))
    a = [3, 2, 1, 7, 6, 5, 4]
    print(sorted(a))


primero()


def main():
    Vocales = ('a', 'e', 'i', 'e', 'a', 'o', 'u', 'a')
    p = Vocales.index('a')
    print(f"La a Aparece en la posicion {p}")
    q = Vocales.index('a', p+1)
    print(f"la segunda a aparece en la posicion {Vocales.index('a',p+1)}")
    print(f"la segunda a aparece en la posicion {Vocales.index('a',q+1)}")


main()


def segundo():

    Vocales = ('a', 'e', 'i', 'e', 'a', 'o', 'u', 'a')
    c = Vocales.count('a')
    print(f"La a aparece {c} veces")


segundo()


def tercero():

    a = (1, 2, 3, 4, 5)
    print(2 in a)
    print(8 in a)

    print("j" in tuple("String"))
    print("j" not in tuple("String"))

    b = (6, 7, 8, 9)

    print(a+b)
    print(b+a)


tercero()

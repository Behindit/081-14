fruta0 = "pera"
fruta1 = "manzana"
fruta2 = "durazno"

print("en la feria compre 1 kg de {0}, 1/2 kg de {1} y 3 kg de {2}")

print("en la feria compre 1 kg de {0}, 1/2 kg de {1} y 3 kg de {2}".format(
    fruta0, fruta1, fruta2)
      )

print("este nummero va completo :{0} y este otro reducido {1:0.2f}".format(
    1.25456, 1.25456))

print("Hola {0:>12}, hola{1:<10}".format("josefina", "Javier"))
print("Hola {0:_>12}, hola{1:_<10}".format("josefina", "Javier"))

nombre = "Javier"
edad = 18
print(f"Hola, {nombre}. Tienes {edad} años")


def main():
    nombre = "JORGE"
    print(f"El nombre {minusculas(nombre)} fue cambiado a minusculas")


def minusculas(nom):
    return nom.lower()


main()


def cuadrados():
    print("Cuadrados y cubos de los primeros 10 enteros positivos: ")
    for i in range(1, 11):
        print(f"{i:5}{i**2:10}{i**3:10}")


cuadrados()

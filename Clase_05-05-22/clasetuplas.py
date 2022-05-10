#Diccionarios

def primero():
    Numeros = {1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro"}
    for i in Numeros:
        print(f"El valor de la clave {i} es {Numeros[i]}")


primero()


def segundo():
    contactos = {"jorge": "9 876 543", "marta": "9 876 543"}
    fono_jorge = contactos["jorge"]
    print(fono_jorge)
    print(contactos)

    l = list(contactos)
    print(f"Primer elemento de \"contactos\":{l[0]}")


segundo()

print("-------------------------------------------------")


def tercero():

    Nuevo = creaDiccionario()
    L = list(Nuevo)
    M = list(Nuevo.values())
    print(L[0])
    N = list(M[0].values())
    print(f"La altura de {L[0]} es: {N[1]}")

    for Estudi in Nuevo:
        print(f"Los datos del estudiante: {Estudi}")
        for Datos in Nuevo[Estudi]:
            print(f"{Datos}: ", Nuevo[Estudi][Datos])


def creaDiccionario():
    Estudiantes = {
        "Jorge": {"Rut": "12.345.678-9", "Altura": 180},
        "Juan": {"Rut": "98.765.432-1", "Altura": 175},
        "Jorge": {"Rut": "56.789.123-4", "Altura": 165}
    }
    return Estudiantes


tercero()

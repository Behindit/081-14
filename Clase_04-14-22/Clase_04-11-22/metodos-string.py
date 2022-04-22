
def cuentacaracteres(f):
    contador = f.count(" ")
    return contador


a = cuentacaracteres("Hola mundo")

print(a)

b = "#Hola#Mundo#"

print(b.strip("#"))

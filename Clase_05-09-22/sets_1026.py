letras = set()
print(letras)

letras2 = set("Hola mundo")
print(letras2)

varias = set(['h', 'a', 'c', 'e', 'r', 12, 3.14, 'chao'])
print(varias)

caracteres = set("uno dos tres cuatro")
print(caracteres)

carac2 = set("caracteres")
print(carac2)

carac2.add(30)
carac2.add("zxcv")
print(carac2)

set1 = set([10, 20, 30, 40])
set2 = set([30, 40, 50, 60])
set3 = set1.union(set2)
set4 = set1 | set2
set5 = set1.intersection(set2)
set6 = set1 & set2
print(set3)
print(set4)
print(set5)
print(set6)

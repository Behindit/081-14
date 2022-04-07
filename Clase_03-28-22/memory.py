a = 5
b = 6

print("a: ", a, " b: ", b)
print(f"{id(a)},{id(b)}")
print("e y f son iguales?: ", a == b)

c = 7
d = 7

print("c: ", c, " d: ", d)
print(f"{id(c)},{id(d)}")
print("e y f son iguales?: ", c == d)

e = 256
f = 256

print("e: ", e, " f: ", f)
print(f"{id(e)},{id(f)}")
print("e y f son iguales?: ", e == f)

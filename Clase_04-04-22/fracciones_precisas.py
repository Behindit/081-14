import fractions

x = fractions.Fraction(15, 5)
z = fractions.Fraction(10, 18)

print(x)
print(z)

# Ejercicio


def main():
    print("Ejercicio A: 7/12 + 15/25")
    x = 7.0/12 + 15.0/25
    print(f"El resultado sin usar fraction es: {x}")
    a = fractions.Fraction(7/12)+fractions.Fraction(15/25)
    print(f"El resultado usando fraction es: {a}")

main()

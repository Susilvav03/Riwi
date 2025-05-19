"""
9. Año Bisiesto
Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

"""

num = int(input("Hola, ingresa el año para determinar si es bisiesto: "))

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año es no es bisiesto")

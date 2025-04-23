"""
2. Número Positivo o Negativo
Pide un número al usuario. Di si es positivo, negativo o si es cero.

"""

num = int(input("Hola, ingresa un número: "))

if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")
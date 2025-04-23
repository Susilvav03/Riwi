"""
7. Mayor de Dos Números
Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

"""

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un número: "))

if num1 > num2:
    print(f"El mayor es {num1}")
elif num2 > num1:
    print(f"El mayor es: {num2}")
else:
    print("Los números son iguales")
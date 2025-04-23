"""
6. Adivina el Número
Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

"""

num = int(input("Ingresa el número que crees que es: "))

secreto = 17

if num > secreto:
    print("El número que has ingresado es mayor al número secreto")
elif num < secreto:
    print("El número que has ingresado es menor al número secreto")
else:
    print("El número que ingresaste... ¡Es igual al número secreto!")
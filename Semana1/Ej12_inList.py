"""
2. Verificar si un número está en una lista

    Crea una lista con 5 números.
    Pide un número al usuario y verifica si está en la lista usando in.

    
"""


lista = [1,3,5,7,9]

intento = int(input("Ingresa un numero:  "))

for i in lista:
    if i == intento:
        print('El número está en la lista')
    
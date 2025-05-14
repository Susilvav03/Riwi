"""
Número par o impar
Crea una función que determine si un número es par o impar.
"""

def oddEven(numero):
    if numero % 2 == 0:
        return "Par"  
    return "Impar"

print(oddEven(10))
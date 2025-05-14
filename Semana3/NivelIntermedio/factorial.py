"""
Factorial
Crea una función que calcule el factorial de un número entero positivo.
"""

def factorial(n):
    if n < 0:
        return "Error: negative number"
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

print(factorial(9))
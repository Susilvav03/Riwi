"""
1. Menor de tres números

    Pide tres números al usuario.
    Usa condicionales (if) para decir cuál es el más pequeño.
    
"""

numero_1 = int(input("Hola! Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))
numero_3 = int(input("Ingresa el tercer numero: "))

if numero_1 <= numero_2 and numero_1 <= numero_3:
    print(f"El numero más pequeño es: {numero_1}")
elif numero_2 <= numero_3 and numero_2 <= numero_1:
    print(f"El numero más pequeño es: {numero_2}")
elif numero_3 <= numero_1 and numero_3 <= numero_2:
    print(f"El numero más pequeño es {numero_3}")
"""
5. Calculadora de Propinas
Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

"""

total = float(input("Hola, ingresa el total de la cuenta "))
propina = int(input("Ingresa el porcentaje de propina a dejar (10, 20, 30) "))

if propina == 10:
    totalPropina = total*0.10
    print(f"El total de la propina a pagar es: {totalPropina}")
elif propina == 15:
    totalPropina = total*0.15
    print(f"El total de la propina a pagar es: {totalPropina}")
elif propina == 20:
    totalPropina = total*0.20
    print(f"El total de la propina a pagar es: {totalPropina}")
else:
    print("El porcentaje ingresado no es valido, debe ser 10, 15 o 20")
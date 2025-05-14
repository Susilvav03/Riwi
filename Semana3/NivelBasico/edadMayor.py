"""
Mayoría de edad
Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.
"""

def ofAge(age):
    if age >= 18:
        return "You are of legal age"  
    return "You are under age"

print(ofAge(17))

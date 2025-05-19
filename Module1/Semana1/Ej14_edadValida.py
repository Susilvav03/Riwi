"""
4. Edad válida

    Pide al usuario su edad.
    Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
    Si está en el rango correcto, imprime "Edad válida".

"""

UserAge = int(input("Hola, por favor ingresa tu edad: "))

if UserAge < 0 or UserAge > 120:
    print("Edad no valida")

else:
    print("Edad valida")

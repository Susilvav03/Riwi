"""
8. Clasificación de IMC

Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

    "Bajo peso" si es menor a 18.5
    "Normal" si está entre 18.5 y 24.9
    "Sobrepeso" si está entre 25 y 29.9
    "Obesidad" si es mayor o igual a 30

"""

peso = float(input("Ingresa tu peso: "))
altu = float(input("Ingresa tu altura: "))
imc = peso / (altu ** 2)
print(imc)
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

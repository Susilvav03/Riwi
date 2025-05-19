"""
Contar vocales
Escribe una función que reciba una cadena y devuelva la cantidad de vocales.
"""

def countVowels(text):
    text = text.lower()
    vowels = "aeiou"
    return sum(1 for letra in text if letra in vowels)

print(countVowels("Susana"))
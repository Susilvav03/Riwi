"""
Palíndromo
Escribe una función que determine si un texto es un palíndromo.
"""

def palindromo(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print(palindromo("Ana"))
"""
Generador de contraseñas
Crea una función que genere una contraseña aleatoria de una longitud dada.
"""

import random
import string

def createPassword(long):
    characteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characteres) for i in range(long))

print(createPassword(8))
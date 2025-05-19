"""
Simular dado
Crea una función que simule el lanzamiento de un dado de 6 caras.
"""

import random

def simDie():
    return random.randint(1, 6)

print(simDie())
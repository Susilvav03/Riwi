"""
Filtrar pares
Crea una función que reciba una lista de números y devuelva solo los pares.
"""

def filterEven(numbers):
    return [num for num in numbers if num % 2 == 0]

list1 = [3,2,9,24,1,45,6]
print(filterEven(list1))
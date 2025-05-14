"""
Suma de elementos únicos
Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.
"""

def sumUniqueElements(elements):
    return sum(set(elements))

list1 = [8,34,5,6,5,37,34,8]
print(sumUniqueElements(list1))
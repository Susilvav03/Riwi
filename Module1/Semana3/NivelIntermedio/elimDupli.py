"""
Eliminar duplicados
Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.
"""

def deleteDuplicate(elements):
    return list(set(elements))


list1 = [8,34,5,6,5,37,34,8]
print(deleteDuplicate(list1))
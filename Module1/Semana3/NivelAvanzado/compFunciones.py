"""
Composición de funciones
Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.
"""

def composicion_funciones(func1, func2):
    return lambda x: func2(func1(x))

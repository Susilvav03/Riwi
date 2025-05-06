"""
Menú:

1. Añadir productos:
Cada producto debe estar definido por su nombre, precio y cantidad disponible (diccionario clave = nombre del producto, valor = (Precio, Cantidad) en una tupla)
Esta información será almacenada de modo que el inventario pueda crecer dinámicamente

2. Consultar productos:
Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
Si el producto no está en el inventario, se debe notificar adecuadamente

3. Actualizar precios:
El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario

4. Eliminar productos:
El programa debe permitir al usuario eliminar productos del inventario de manera segura

5. Calcular el valor total del inventario:
El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.

*** Manejo de errores ***
El programa debe manejar errores de entrada del usuario
- Intentar añadir un producto con un precio o cantidad negativa
- Intentar buscar productos que no existeny en el inventario
- Intentar actualizar el precio de un producto que no existe
- Intentar eliminar un producto que no existe
- Contador de intentos de añadir productos con datos inválidos

"""

flag = True
inventory = {}
count = 0

# Función para mostrar menú y obtener la opción del usuario
def menu():
    print("------------------------------------------------")
    print("Bienvenido al sistema de gestión de inventario")
    print("--------------------- Menú ---------------------")
    print("1. Añadir productos")
    print("2. Consultar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Calcular el valor total del inventario")
    print("6. Salir")
    print("------------------------------------------------")

    return input("Seleccione una opción: ")

# Función para añadir productos al inventario 
def añadir_producto(inventory):
    global count
    # Se inicializa el contador de intentos
    count = 0
    # Se permite un máximo de 3 intentos para añadir un producto
    while count < 3:
        try:
            # Se solicita al usuario el nombre, precio y cantidad del producto
            productName = input("Ingrese el nombre del producto: ")

            # Se valida que el nombre del producto no esté vacío
            if not productName.strip():
                print("Error: El nombre del producto no puede estar vacío.")
                count += 1
                return
            
            price = float(input("Ingrese el precio del producto: "))
            quantity = int(input("Ingrese la cantidad disponible: "))

            # Se valida que el precio y la cantidad sean mayores que cero
            if price < 0 or quantity < 0:
                print("Error: El precio y la cantidad deben ser mayores que cero.")
                count += 1
                return

            # Se verifica si el producto ya existe en el inventario
            if productName in inventory:
                print(f"El producto '{productName}' ya existe en el inventario.")
                count += 1
                return
            
            # Se añade el producto al inventario
            inventory[productName] = (price, quantity)
            print(f"Producto '{productName}' añadido con éxito.")
            break
        except ValueError:
            # Máximo de 3 intentos para ingresar datos válidos
            print("Error: Entrada inválida. Por favor, intente de nuevo.")
            count += 1
            if count >= 3:
                print("Demasiados intentos fallidos. Saliendo del programa.")
                exit()

# Función para consultar productos en el inventario
def consultar_producto(inventory):
    productName = input("Ingrese el nombre del producto a consultar: ")
    # Se verifica si el producto existe en el inventario
    if productName in inventory:
        price, quantity = inventory[productName]
        print(f"Producto: {productName}, Precio: {price}, Cantidad: {quantity}")
    else:
        print(f"El producto '{productName}' no se encuentra en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio(inventory):
    productName = input("Ingrese el nombre del producto a actualizar: ")
    # Se verifica si el producto existe en el inventario
    if productName in inventory:
        try:
            newPrice = float(input("Ingrese el nuevo precio: "))
            # Se valida que el nuevo precio sea mayor que cero
            if newPrice < 0:
                print("Error: El nuevo precio debe ser mayor que cero.")
                return
            # Se actualiza el precio del producto en el inventario
            price, quantity = inventory[productName]
            inventory[productName] = (newPrice, quantity)
            print(f"El precio del producto '{productName}' ha sido actualizado a {newPrice}.")
        except ValueError:
            print("Error: Entrada inválida. Por favor, intente de nuevo.")
    else:
        print(f"El producto '{productName}' no se encuentra en el inventario.")

# Función para eliminar un producto del inventario
def eliminar_producto(inventory):
    productName = input("Ingrese el nombre del producto a eliminar: ")
    # Se verifica si el producto existe en el inventario
    if productName in inventory:
        del inventory[productName]
        print(f"El producto '{productName}' ha sido eliminado del inventario.")
    else:
        print(f"El producto '{productName}' no se encuentra en el inventario.")

# Función para calcular el valor total del inventario
def calcular_valor_total(inventory):
    # Se utiliza una función lambda para calcular el valor total
    total_value = sum(map(lambda x: x[0] * x[1], inventory.values()))
    print(f"El valor total del inventario es: {total_value}")

# Bucle principal del programa
while flag:
    option = menu()
    match option:
        case '1':
            añadir_producto(inventory)
        case '2':
            consultar_producto(inventory)
        case '3':
            actualizar_precio(inventory)
        case '4':
            eliminar_producto(inventory)
        case '5':
            calcular_valor_total(inventory)
        case '6':
            print("Saliendo del programa...")
            flag = False
        case _:
            print("Opción inválida. Por favor, intente de nuevo.")

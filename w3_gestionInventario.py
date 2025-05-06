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
- El programa debe manejar errores de entrada del usuario
- Intentar añadir un producto con un precio o cantidad negativa
- Intentar buscar productos que no existen en el inventario
- Intentar actualizar el precio de un producto que no existe
- Intentar eliminar un producto que no existe
- Contador de intentos de añadir productos con datos inválidos

"""
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
flag = True
inventory = {}

# Función para mostrar menú y obtener la opción del usuario
def menu():
    print(MAGENTA + "\n _________________________________________________" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|  Bienvenido al sistema de gestión de inventario |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|---------------------- Menú ---------------------|" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "| 1. Añadir productos                             |" + RESET)
    print(MAGENTA + "| 2. Consultar productos                          |" + RESET)
    print(MAGENTA + "| 3. Actualizar precios                           |" + RESET)
    print(MAGENTA + "| 4. Eliminar productos                           |" + RESET)
    print(MAGENTA + "| 5. Calcular el valor total del inventario       |" + RESET)
    print(MAGENTA + "| 6. Salir                                        |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)

    return input("\nSeleccione una opción: ")

# Función para añadir productos al inventario 
def addProduct(inventory):
    # Se inicializa el contador de intentos
    count = 0
    # Se permite un máximo de 3 intentos para añadir un producto
    while count < 3:
        try:
            productName = input("\nIngrese el nombre del producto: ")

            # Se valida que el nombre del producto no esté vacío
            if not productName.strip():
                print(YELLOW + "Error: El nombre del producto no puede estar vacío." + RESET)
                count += 1
                continue
            
            price = int(input("\nIngrese el precio del producto: $"))

            # Se valida que el precio sea mayor que cero
            if price < 0:
                print(YELLOW + "Error: El precio debe ser mayor que cero." + RESET)
                count += 1
                continue

            quantity = int(input("\nIngrese la cantidad disponible: "))

            # Se valida que la cantidad sea mayor que cero
            if quantity < 0:
                print(YELLOW + "Error: la cantidad debe ser mayor que cero." + RESET)
                count += 1
                continue

            # Se verifica si el producto ya existe en el inventario
            if productName in inventory:
                print(YELLOW + f"\nEl producto '{productName}' ya existe en el inventario." + RESET)
                count += 1
                continue
            
            # Se añade el producto al inventario
            inventory[productName] = (price, quantity)
            print(GREEN + f"\nProducto '{productName}' se ha añadido con éxito." + RESET)
            break
        except ValueError:
            # Errores
            print(YELLOW + "Error: Entrada inválida. Por favor, intente de nuevo, debe ingresar un número entero" + RESET)
            count += 1
    else:
        # Máximo de 3 intentos para ingresar datos válidos
        print(RED + "\n __________________________________________________ " + RESET)
        print(RED + "|                                                  |" + RESET)
        print(RED + "|  Demasiados intentos fallidos. Volviendo al menú.|" + RESET)
        print(RED + "|__________________________________________________|" + RESET)
        return
        

# Función para consultar productos en el inventario
def searchProduct(inventory):
    productName = input("\nIngrese el nombre del producto a consultar: ")
    # Se verifica si el producto existe en el inventario
    if productName in inventory:
        price, quantity = inventory[productName]
        print(GREEN + f"""
    Producto: {productName} 
    Precio:   ${price} 
    Cantidad: {quantity}""" + RESET)
    else:
        print(YELLOW + f"\nEl producto '{productName}' no se encuentra en el inventario." + RESET)

# Función para actualizar el precio de un producto
def updatePrice(inventory):
    # Se inicializa el contador de intentos
    count = 0

    while count < 3:
        productName = input("\nIngrese el nombre del producto a actualizar: ")

        # Se verifica si el producto existe en el inventario
        if productName in inventory:
            try:
                newPrice = int(input("Ingrese el nuevo precio: $"))
                # Se valida que el nuevo precio sea mayor que cero
                if newPrice < 0:
                    print(YELLOW + "Error: El nuevo precio debe ser mayor que cero." + RESET)
                    count += 1
                    continue
                # Se actualiza el precio del producto en el inventario
                price, quantity = inventory[productName]
                inventory[productName] = (newPrice, quantity)
                print(GREEN + f"\nEl precio del producto '{productName}' ha sido actualizado a ${newPrice}." + RESET)
                break
            except ValueError:
                print(YELLOW + "Error: Entrada inválida. Por favor, intente de nuevo, debe ingresar un número entero" + RESET)
                count += 1
                continue
        else:
            print(YELLOW + f"\nEl producto '{productName}' no se encuentra en el inventario." + RESET)
            return  
    else:
        # Máximo de 3 intentos para ingresar datos válidos
        print(RED + "\n __________________________________________________ " + RESET)
        print(RED + "|                                                  |" + RESET)
        print(RED + "|  Demasiados intentos fallidos. Volviendo al menú.|" + RESET)
        print(RED + "|__________________________________________________|" + RESET)
        return

# Función para eliminar un producto del inventario
def deleteProduct(inventory):
    productName = input("\nIngrese el nombre del producto a eliminar: ")
    # Se verifica si el producto existe en el inventario
    if productName in inventory:
        del inventory[productName]
        print(GREEN + f"\nEl producto '{productName}' ha sido eliminado del inventario." + RESET)
    else:
        print(YELLOW + f"\nEl producto '{productName}' no se encuentra en el inventario." + RESET)

# Función para calcular el valor total del inventario
def calculateTotal(inventory):
    # Se utiliza una función lambda para calcular el valor total
    total_value = sum(map(lambda x: x[0] * x[1], inventory.values()))
    print(GREEN + f"\nEl valor total del inventario es: ${total_value}" + RESET)

# Bucle principal del programa
while flag:
    option = menu()
    match option:
        case '1':
            addProduct(inventory)
        case '2':
            searchProduct(inventory)
        case '3':
            updatePrice(inventory)
        case '4':
            deleteProduct(inventory)
        case '5':
            calculateTotal(inventory)
        case '6':
            print("\n...Saliendo del programa...")
            flag = False
        case _:
            print("\nOpción inválida. Por favor, ingresa un número del 1 al 6 de acuerdo a lo que desees hacer.")

"""
Menú de gestión de inventario:

- Añadir productos:  (con parámetros para nombre, precio y cantidad)
a. Cada producto debe estar definido por su nombre, precio y cantidad disponible
b. Esta información será almacenada de modo que el inventario pueda crecer dinámicamente (diccionario clave = nombre del producto, valor = (Precio, Cantidad) en una tupla)

- Consultar productos: (con parametro nombre y retorno de precio y cantidad)
a. Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
b. Si el producto no está en el inventario, se debe notificar adecuadamente

- Actualizar precios: (con parámetros para nombre y precio)
a. El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario

- Eliminar productos: (con parámetro para nombre)
a. El programa debe permitir al usuario eliminar productos del inventario de manera segura

- Calcular el valor total del inventario: (Función anónima)
a. El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario

- Salir

*** Manejo de errores ***
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

def menu():
    """ Mostrar el menú """
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

def validatePositive(value):
    """ Validar que el valor sea positivo """
    if value.isdigit() and float(value) > 0:
        return True, None
    
    return False, "El valor ingresado debe ser un número positivo"

def validateInventory(name):
    """ Validar que el producto exista en el inventario """
    if name in inventory:
        return True, f"El producto '{name}' existe en el inventario." 
    
    return False, f"El producto '{name}' no existe en el inventario" 
    
def errorMessage():
    """ Mostrar mensaje de error al llegar a 3 intentos """
    print(RED + "\n __________________________________________________ " + RESET)
    print(RED + "|                                                  |" + RESET)
    print(RED + "|  Demasiados intentos fallidos. Volviendo al menú.|" + RESET)
    print(RED + "|__________________________________________________|" + RESET)
    

def addProduct(name, price, quantity):
    """ Añadir un producto al inventario """
    inventory[name] = (price, quantity)
    print(GREEN + f"Producto '{name}' ha sido añadido al inventario exitosamente" + RESET)

def searchProduct(name):
    """ Buscar un producto en el inventario e imprimir su precio y cantidad """
    price, quantity = inventory[name]
    print(GREEN + f"""
        Producto '{name}' encontrado: 
        Precio: ${price}, 
        Cantidad: {quantity}""" + RESET)

def updatePrice(name, newPrice):
    """ Actualizar el precio de un producto """
    price, quantity = inventory[name]
    inventory[name] = (newPrice, quantity)
    print(GREEN + f"El precio del producto '{name}' ha sido actualizado de ${price} a ${newPrice}." + RESET)

def deleteProduct(name):
    """ Eliminar un producto del inventario """
    del inventory[name]
    print(GREEN + f"Producto '{name}' ha sido eliminado del inventario." + RESET)

def calculateTotalValue():
    """ Calcular el valor total del inventario """
    total_value = sum(map(lambda x: x[0] * x[1], inventory.values()))
    print(GREEN + f"\nEl valor total del inventario es: ${total_value}" + RESET)


# Bucle principal
while flag:
    menu()

    #Elegir opción del menú
    option = input("\nSeleccione una opción: ")

    match option:
        # Opción 1: Añadir Productos
        case "1":
            # Contador de intentos para ingresar un nombre que no exista y un precio y cantidad que sean > 0, maximo permitido = 3
            i=0
            while i < 3:
                name = input("\nIngrese el nombre del producto: ")
                val, msg = validateInventory(name)
                if val:
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                price = input("\nIngrese el precio del producto: ")
                val, msg = validatePositive(price)
                if not val:
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                quantity = input("\nIngrese la cantidad del producto: ")
                val, msg = validatePositive(quantity)
                if not val:
                    print(YELLOW + msg + RESET)
                    i += 1
                    continue
                if addProduct(name, price, quantity):
                    break
            else:
                errorMessage()
        # Opción 2: Consultar Productos
        case "2":
            name = input("\nIngrese el nombre del producto a consultar: ")
            val, msg = validateInventory(name)
            if val:
                searchProduct(name)
            else:
                print(RED + msg + RESET)
        # Opción 3: Actualizar Precio
        case "3":
            name = input("\nIngrese el nombre del producto a actualizar: ")
            val, msg = validateInventory(name)
            if not val:
                print(RED + msg + RESET)
            else: 
                # Contador de intentos para ingresar precio, máximo permitido = 3
                i=0
                while i < 3:
                    newPrice = input("\nIngrese el nuevo precio del producto: ")
                    val, msg = validatePositive(newPrice)
                    if not val:
                        print(YELLOW + msg + RESET)
                        i += 1
                        continue
                    if updatePrice(name, newPrice):
                        break
                else:
                    errorMessage()
        # Opción 4: Eliminar producto 
        case "4":
            name = input("\nIngrese el nombre del producto a eliminar: ")
            val, msg = validateInventory(name)
            if not val:
                print(RED + msg + RESET)
            else:
                deleteProduct(name)
        # Opción 5: Cálcular valor total del inventario
        case "5":
            calculateTotalValue()
        # Opción 6: Salir
        case "6":
            print(GREEN + "\nGracias por usar el sistema de gestión de inventario. ¡Hasta luego!" + RESET)
            flag = False
        # Opción no valida     
        case _:
            print(RED + "\nOpción no válida. Por favor, seleccione una opción del menú." + RESET)
            

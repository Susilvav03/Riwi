print("Sistema de validación de productos") # Programa
productList = [] # Crear lista donde se almacenarán los productos
addProduct = "si" # Inicialmente esta variable empezará como si pero podrá cambiar

# Se iniciará el programa siempre y cuando la variable addProduct sea igual a si, de lo contrario procederá a mostrar los productos
while (addProduct.lower() == "si"):

    print("\n--- Nuevo Producto ---") # Separador

    productName = input("Ingresa el nombre del producto: ") # Se inicializa la variable donde se guardará el nombre del producto y se le pide al usuario

    # Validación de que el valor ingresado en price sea un flotante positivo
    while True: 
        try:
            price = float(input("Ingresa el precio unitario: ")) # Se inicializa la variable donde se guardará el precio del producto y se le pide al usuario
            if (0 <= price):  # Validación de que está entrando un número positivo  
                break # Salir del bucle
            else:
                print("Ingresa un número positivo") # Si no está ingresando un número positivo, debe volverlo a intentar
        except ValueError:
            print("¡Ingresa un número valido!") # Aparecerá en caso de que el usuario ingrese un valor no flotante, debe volverlo a intentar

    # Validación de que el valor ingresado en cant sea un entero positivo
    while True: 
        try:        
            cant = int(input(f"Ingresa la cantidad de {productName} que vas a comprar: ")) # Se inicializa la variable donde se guardará la cantidad del producto y se le pide al usuario
            if (0 <= cant): # Validación de que está entrando un número positivo  
                break # Salir del bucle
            else:
                print("Ingresa un número positivo") # Aparecerá sii no está ingresando un número positivo, debe volverlo a intentar
        except ValueError:
            print("¡Ingresa un número valido!") # Aparecerá en caso de que el usuario ingrese un valor no entero, debe volverlo a intentar
    
    total = price * cant  # Cálculo del precio total sin descuento

    # Validación de que la entrada de descuento si sea alguna de las opciones (si/SI/Si/sI) ó (no/NO/No/nO)
    while True: 
        try:
            descuento = input("¿El producto tiene descuento? (Si/No) ") # Se inicializa la variable donde se guardará si el producto tiene descuento o no
            if (descuento.lower() == "si") or (descuento.lower() == "no"): # Alguna de las dos opciones se debe cumplir
                break # Salir del bucle
            else:
                 print("Debes escoger Si o No, intenta de nuevo") # Aparecerá en caso de que el usuario ingrese un texto diferente a (si/SI/Si/sI) ó (no/NO/No/nO), debe volverlo a intentar
        except ValueError:
            continue # En caso de error, debe volverlo a intentar


    if (descuento.lower() == "si"): # En caso de que si haya descuento

        # Validación de que el % de descuento es un número entero mayor a 0 y menor o igual a 100
        while True: 
            try:
                desc = int(input("Ingresa el porcentaje de descuento: ")) # Se inicializa la variable donde se guardará el % del descuento
                if (0 < desc <= 100): # Condición de dato valido para el descuento
                    totald = price * cant - (price*cant*(desc/100)) # Cálculo del precio total con descuento
                    break # Salir del bucle
                else:
                    print("El número ingresado debe ser mayor a 0 y menor o igual a 100, intenta de nuevo") # Aparecerá si el valor ingresado en desc es un entero por fuera del rango valido, debe volverlo a intentar
            except ValueError:
                print("Debes ingresar un número entero, intenta de nuevo") # Aparecerá si el valor ingresado en desc es un valor no entero, debe volverlo a intentar
    else:
        totald = total # Si no hay descuento, el precio total con descuento es el mismo al precio total sin descuento

    # Creación de diccionario para almacenar la información del producto
    product = {
        "Producto": productName,
        "Precio_unitario": price,
        "Cantidad_producto": cant,
        "Total": total,
        "Total_descuento": totald
    }

    productList.append(product) # Agregar el diccionario a la lista de productos
    # Validación de que la entrada para añadir otro producto si sea alguna de las opciones (si/SI/Si/sI) ó (no/NO/No/nO)
    while True: 
        try:
            addProduct = input("¿Quieres añadir otro producto? (Si/No) ") # Se inicializa la variable donde se guardará si el usuario quiere añadir otro producto
            if (addProduct.lower() == "si") or (addProduct.lower() == "no"): # Alguna de las dos opciones se debe cumplir
                break # Salir del bucle
            else:
                 print("Debes escoger Si o No, intenta de nuevo") # Aparecerá en caso de que el usuario ingrese un texto diferente a (si/SI/Si/sI) ó (no/NO/No/nO), debe volverlo a intentar
        except ValueError:
            continue # En caso de error, debe volverlo a intentar

print("\nProductos registrados:") # Separador para empezar a enlistar

# Imprimir los datos de cada producto llamando a productList y buscando dentro de cada diccionario de cada producto
for product in productList:
    print(f"""
        ------------------------------------
        Producto             => {product['Producto']}
        Precio Unitario      => ${product['Precio_unitario']:.2f}
        Cantidad             => {product['Cantidad_producto']}
        Precio Normal        => ${product['Total']:.2f}
        Precio Total         => ${product['Total_descuento']:.2f}
        ------------------------------------
    """)
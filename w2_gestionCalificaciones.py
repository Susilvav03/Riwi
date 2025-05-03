"""

Opciones:

1. Determinar si aprobó:
    Utiliza if, if-else e if-elif-else para determinar el estado 
    de aprobación y mostrar mensajes adecuados
    
    a. Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    b. Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

2. Calcular el promedio:
    Implementa un ciclo for para recorrer la lista de calificaciones 
    y calcular el promedio
    
    a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    b. Calcular y mostrar el promedio de las calificaciones en la lista

3. Contar calificaciones mayores a:
    Usa un ciclo while para contar cuántas calificaciones son mayores 
    que el valor especificado

    a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    b. Preguntar al usuario por un valor específico
    c. Contar cuántas calificaciones en la lista son mayores que este valor

4. Contar calificaciones iguales a:
    Emplea un ciclo for para verificar la presencia de una calificación 
    específica y contar cuántas veces aparece, utilizando break y continue 
    para controlar el flujo
    
    a. Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    b. Preguntar al usuario por un valor específico
    c. Contar cuántas calificaciones en la lista son iguales a este valor

    
"""

print("\n         Sistema de Gestión de Calificaciones")

# Declarar la variable con la que se repetirá el ciclo
flag = True
# Ciclo para repetir el programa
while flag:
    
    # Mostrar las opciones al usuario
    print("\n--------------------- OPCIONES ---------------------")
    print("1. Determinar si aprobó")
    print("2. Calcular el promedio")
    print("3. Contar calificaciones mayores a cierto valor")
    print("4. Contar calificaciones iguales a cierto valor")
    print("5. Salir")
    print("----------------------------------------------------")
    
    # Solicitar al usuario que elija una opción
    option = int(input("\n¿Qué deseas hacer? elige un número del 1 al 5: "))
    
    
    # Verificar la opción elegida
    match option:
        case 1:
            print("\n-------------------- ¿APROBASTE? --------------------")
            # Validación de errores
            while flag:
                try:
                    # Solicitar al usuario que ingrese la calificación
                    grade = int(input("Ingresa tu calificación: "))
                    #V alidación de rango
                    if (0 <= grade <= 100):
                        # Determinar el estado de aprobación
                        if grade >= 70:
                            print(f"Tu nota fue {grade} ¡Aprobaste!")
                            break
                        elif grade >= 60:
                            print(f"Tu nota fue {grade} ¡Casi apruebas! pero puedes aplicar a un examen de recuperación")
                            break
                        else:
                            print(f"Tu nota fue {grade} ¡Reprobaste!")
                            break
                    else:
                        print("Ingresa un número de 0 a 100, intenta de nuevo")
                        continue
                except ValueError:
                    print("Ingresa un número entero")
        case 2:
            print("\n---------------- CALCULAR PROMEDIO -----------------")
            # Validación de errores
            while flag:
                try:
                    # Solicitar al usuario que ingrese una lista de calificaciones
                    grades = input("Ingresa las calificaciones separadas por comas: ")
                    # Convertir la cadena de calificaciones en una lista de números
                    list_grades = [int(cal) for cal in grades.split(",")]
                    
                    # Validación de rango
                    if any(cal < 0 or cal > 100 for cal in list_grades):
                        print("Ingresa solo números entre 0 y 100. Intenta de nuevo.")
                        continue
                        
                    # Calcular el promedio
                    prom = sum(list_grades) / len(list_grades)
                    # Mostrar el promedio
                    print(f"El promedio de las calificaciones es: {prom:.2f}")
                    break
                except ValueError:
                    print("Ingresa números enteros en la lista, intenta de nuevo")
        case 3:
            print("\n--------- CONTAR CALIFICACIONES MAYORES A ----------")
            # Validación de errores
            while flag:
                try:
                    # Solicitar al usuario que ingrese una lista de calificaciones
                    grades = input("Ingresa las calificaciones separadas por comas: ")
                    # Convertir la cadena de calificaciones en una lista de números
                    list_grades = [int(cal) for cal in grades.split(",")]
                    
                    # Validación de rango
                    if any(cal < 0 or cal > 100 for cal in list_grades):
                        print("Ingresa solo números entre 0 y 100. Intenta de nuevo.")
                        continue
                    # Solicitar el valor específico
                    grade = int(input("Ingresa el valor específico: "))
                    # Validación de rango
                    if (grade < 0 or grade > 100):
                        print("Ingresa un número de 0 a 100, intenta de nuevo")
                        continue
                    # Contar cuántas calificaciones son mayores que el valor específico
                    i = 0
                    for cal in list_grades:
                        if cal > grade:
                            i += 1
                    # Mostrar el resultado
                    print(f"Hay {i} calificaciones mayores a {grade}")
                    break
                except ValueError:
                    print("Ingresa números enteros en la lista y en el valor específico, intenta de nuevo")
        case 4:
            print("\n--------- CONTAR CALIFICACIONES IGUALES A ----------")
            # Validación de errores
            while flag:
                try:
                    # Solicitar al usuario que ingrese una lista de calificaciones
                    grades = input("Ingresa las calificaciones separadas por comas: ")
                    # Convertir la cadena de calificaciones en una lista de números
                    list_grades = [int(cal) for cal in grades.split(",")]
                    # Validación de rango
                    if any(cal < 0 or cal > 100 for cal in list_grades):
                        print("Ingresa solo números entre 0 y 100. Intenta de nuevo.")
                        continue
                    # Solicitar el valor específico
                    grade = int(input("Ingresa el valor específico: "))
                    # Validación de rango
                    if (grade < 0 or grade > 100):
                        print("Ingresa un número de 0 a 100, intenta de nuevo")
                        continue
                    # Contar cuántas veces aparece la calificación específica
                    i = 0
                    for cal in list_grades:
                        if cal == grade:
                            i += 1
                    # Mostrar el resultado
                    print(f"La calificación {grade} aparece {i} veces")
                    break
                except ValueError:
                    print("Ingresa números enteros en la lista y en el valor específico, intenta de nuevo")
        case 5:
            flag = False
        
        case _:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
else:            
# Fin del programa
    print("\n¡Hasta luego!")






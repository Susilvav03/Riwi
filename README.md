# 🔵 Fundamentos

#### ¿Qué es programar?
Es dar instrucciones a una computadora para que realice una tarea en específico.

#### ¿Qué es Python y para qué sirve?
Python es un lenguaje de programación de alto nivel y multiparadigma que sirve para realizar distintos tipos de programas como aplicaciones o para manejo de datos.

#### ¿Qué es un programa y cómo se ejecuta?
Un programa es un conjunto de instrucciones que una computadora puede seguir para realizar una tarea específica, se puede ejecutar con un interprete o un compilador.

#### ¿Qué es una variable?
Una variablee es como una cajita en donde puedes guardar datos para usar más adelante.

#### Tipos de datos básicos: 
texto (str), número entero (int), número decimal (float), verdadero/falso (bool).

#### Operaciones básicas con números 
+, -, *, /.

#### Mostrar información en pantalla: 
print().

#### Pedir información al usuario: 
input().

#### Convertir tipos de datos: 
int(), float(), str().

#### ¿Qué es un error? Errores comunes para principiantes.
Un error es cuando algo sale mal a la hora de ejecutar el código, algunos errores comunes son:
- Error de sintaxis, ej: no cerrar un parentesis.
- Error de nombre, ej: no definir una variable o si definirla pero escribir mal el nombre.
- Error de tipo, ej: Intentar sumar texto con un número.
- Error de identación, ej: la tabulación no se hizo y el print está a la izquierda de donde debería por lo que no esta entrando en el if.

#### ¿Qué es una lista y para qué sirve?
Una lista es una estructura de datos que sirve para almacenar varios elementos de diferente tipo en una sola variable y poder acceder a ellos para agregar, eliminar y cambiar valores.

#### Crear listas: 
    Lista = [ ]

#### Acceder a elementos de una lista 
    (miLista[0])
- En el indice utilizar ":", ej: miLista([3:7]), esto estaría escogiendo una sección de la lista desde la posición 3 (inclusive) hasta la posición 7 (no inclusive)

## Modificar elementos de una lista

#### Agregar elementos a una lista: 
- .append(): Agrega un elemento al final de la lista.
- .insert(): Agrega un elemento en una posición específica (índice).
- .extend(): Agrega varios elementos de otra lista (o cualquier iterable).

#### Eliminar elementos de una lista: 
- .remove(): Elimina la primera aparición del valor que le digas.
- .pop(): Elimina el elemento en la posición que indiques. Si no pones nada, elimina el último.
- .clear(): Borra todos los elementos de la lista.
- del: Elimina el elemento en una posición específica, similar a pop.

#### Editar elementos de una lista:
    miLista[indice] = nuevo_valor
  
#### Conocer la cantidad de elementos: 
    len().

#### Recorrer listas:
Con un for

# 🔵 Lógica de programación

#### Comparar datos: 
== (igual), != (diferente), < (menor que), > (mayor que), <= (menor o igual que), >= (mayor o igual que).

#### Tomar decisiones: 
if (sí condicional), else (sino), elif (sino si).

#### Combinar condiciones: 
and (ambas se deben cumplir), or (alguna de las dos se debe cumplir), not(negación).

#### ¿Cómo escribir comentarios en el código?
#comentario.

#### ¿Qué es la indentación y por qué es tan importante en Python?
La indentación es el uso de espacios o tabulaciones al principio de una línea de código para indicar qué bloques de código pertenecen a qué estructuras. 
En Python, la indentación es esencial para definir la jerarquía o estructura del programa.

#### Buenas prácticas al nombrar variables 
nombres claros y sin espacios.

#### ¿Qué hacer cuando algo no funciona? 
buscar, leer errores, no frustrarse.

#### ¿Qué es un bucle anidado?
Es cuando un bucle está dentro de otro bucle. Ej: un for o while que corre dentro de otro for o while.

#### ¿Cómo funcionan los índices y rangos en listas (range())?
- Los índices son los números que indican la posición de los elementos dentro de una lista y empiezan desde 0 (si se recorre de izquierda a derecha), o desde -1 (si se recorre de derecha a izquierda).
- range() genera una secuencia de números, ideal para usar en bucles for (range(inicio, fin, paso))

  ejemplo:

      for i in range(len(miLista)):
  
## Introducción a las funciones

#### ¿Qué es una función y por qué usarlas?
Una función es un bloque de código reutilizable que hace una tarea específica. Se puede "llamar" (usar) cada vez que se necesite esa tarea, sin tener que escribir el mismo código una y otra vez.

#### Definir funciones: 
Se usa la palabra clave def, seguida del nombre de la función, paréntesis () (donde se ponen los parámetros) y dos puntos :. 
Luego va el bloque de código que se ejecutará cuando se llame la función.

#### Llamar (usar) funciones:
Se usa su nombre seguido de paréntesis. Si la función tiene parámetros, se debe pasar dentro de los paréntesis.

#### Parámetros y argumentos en funciones:
- Los Parámetros son variables que sse definen dentro de una función,los parámetros actúan como "espacios reservados" para los valores que se pasarán cuando se llame a la función.
- Los Argumentos son los valores reales que se pasan a la función cuando se llama, esos valores se asignan a los parámetros definidos dentro de la función.
  
#### ¿Qué es el retorno de una función?
El retorno es el valor que una función devuelve cuando termina de ejecutar, se usa la palabra clave return para devolver un valor desde una función.
- Cuando una función termina, si tiene un return, ese valor se "devuelve" al lugar donde fue llamada la función.
- Si una función no tiene return, no devolverá nada, y su valor por defecto será None.


# 🔵 Estructuras de control

#### Repetir acciones con bucles: 
for (condicional para) y while (condicional mientras).

#### Salir de un bucle antes de tiempo: 
- break: permite terminar la ejecución de un bucle antes de que haya recorrido todos los elementos en el momento que se cumpla una condición.
- continue: se utiliza para saltar el resto del código en la iteración actual del bucle y continuar con la siguiente iteración. Es decir, no se ejecuta el código que sigue al continue, pero el bucle no se detiene.

#### Manejo básico de errores: 
try-except: permite capturar excepciones (errores) y manejarlas de manera controlada, evitando que el programa se detenga inesperadamente.
- try: Bloque de código donde intentas ejecutar algo que podría generar un error.
- except: Bloque de código que se ejecuta si ocurre un error en el bloque try, si no ocurre ningún error en el bloque try, el bloque except se salta. Con múltiples bloques except se puede especificar diferentes reacciones para diferentes errores.
- else: se ejecuta si no ocurre ningún error en el bloque try.
- finally: siempre se ejecuta sin importar si hubo o no un error. Se usa para limpiar recursos o realizar tareas importantes, como cerrar archivos, liberar memoria, etc.

  ejemplo:
  
      try:
        numero = int(input("Introduce un número: "))
        resultado = 10 / numero
      except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
      except ValueError:
        print("Error: Entrada no válida, por favor introduce un número.")
      else:
        print(f"El resultado de la división es: {resultado}")
      finally:
        print("Este bloque siempre se ejecuta.")



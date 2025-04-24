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
- (miLista[0])
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

#### Cómo escribir comentarios en el código 
#comentario.

#### Qué es la indentación y por qué es tan importante en Python.
La indentación es el uso de espacios o tabulaciones al principio de una línea de código para indicar qué bloques de código pertenecen a qué estructuras. 
En Python, la indentación es esencial para definir la jerarquía o estructura del programa.

#### Buenas prácticas al nombrar variables 
nombres claros y sin espacios.

#### ¿Qué hacer cuando algo no funciona? 
buscar, leer errores, no frustrarse.

# 🔵 Estructuras de control

#### Repetir acciones con bucles: 
for (condicional para) y while (condicional mientras).

#### Salir de un bucle antes de tiempo: 
break y continue.

#### Manejo básico de errores: 
try-except.


"""
5. ¿Está en la lista de invitados?

    Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
    Pide al usuario su nombre.
    Usa if para decir si está en la lista de invitados o no.
    
"""

InvitedList = ["Luis Cepeda", "Susana Silva", "Mateo Zapata", "Sulderi Vallejo", "Pepito Perez", "Fulano Detal"]

UserName = input("Ingresa tu nombre para ver si estás invitado: ")

if UserName in InvitedList:
    print("¡Estás invitado!")

else:
    print("No te han invitado :c")

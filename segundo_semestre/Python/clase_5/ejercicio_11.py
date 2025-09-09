# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#     1. Nuevo contacto
#     2. Borrar contacto
#     3. Ver contactos existentes
#     4. Salir

# Diccionario vacío para almacenar los contactos
agenda = {}

while True:
    # Mostrar el menú
    print("\n===== AGENDA TELEFÓNICA =====")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")

    # Leer opción del usuario
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        # Agregar un nuevo contacto
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")

        if nombre in agenda:
            print(f" El contacto '{nombre}' ya existe.")
        else:
            agenda[nombre] = telefono
            print(f" Contacto '{nombre}' agregado con éxito.")

    elif opcion == "2":
        # Borrar contacto
        nombre = input("Ingrese el nombre del contacto a borrar: ")

        if nombre in agenda:
            del agenda[nombre]
            print(f" Contacto '{nombre}' borrado.")
        else:
            print(f"El contacto '{nombre}' no existe.")

    elif opcion == "3":
        # Mostrar contactos
        if agenda:
            print("\n Contactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"- {nombre}: {telefono}")
        else:
            print(" La agenda está vacía.")

    elif opcion == "4":
        # Salir del programa
        print(" Saliendo de la agenda... ¡Hasta luego!")
        break

    else:
        print(" Opción no válida. Intente de nuevo.")
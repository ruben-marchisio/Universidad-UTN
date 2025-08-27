#Diseñar un programa que ingresando un año, nos devuelva por consola si es un año bisiesto o no.
#repetir la accion hasta que el usuatio decida salir.

while True:
    # Pedir al usuario que ingrese un año
    año = int(input("Ingrese un año (o 0 para salir): "))

    # Si el usuario ingresa 0, se termina el programa
    if año == 0:
        print("¡Programa finalizado!")
        break

    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} NO es bisiesto.")


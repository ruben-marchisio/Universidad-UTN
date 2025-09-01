# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de 1000$ y tendrá el siguiente menú de opciones:
#
#     1. Ingresar dinero en la cuenta
#     2. Retirar dinero de la cuenta
#     3. Mostrar dinero disponible
#     4. Salir

# 1. Saldo inicial
saldo = 1000

while True:
    # 2. Mostrar menú
    print("\n===== Cajero Automático =====")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    # 3. Pedir opción al usuario
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        # Ingresar dinero
        ingreso = float(input("Ingrese la cantidad a depositar: "))
        saldo += ingreso
        print(f"✅ Se han ingresado ${ingreso}. Nuevo saldo: ${saldo}")

    elif opcion == "2":
        # Retirar dinero
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("❌ No tienes suficiente saldo.")
        else:
            saldo -= retiro
            print(f"✅ Has retirado ${retiro}. Nuevo saldo: ${saldo}")

    elif opcion == "3":
        # Mostrar saldo
        print(f"💰 Dinero disponible: ${saldo}")

    elif opcion == "4":
        # Salir
        print("👋 Gracias por usar el cajero. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción inválida. Intente de nuevo.")
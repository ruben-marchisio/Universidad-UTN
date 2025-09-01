# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

import random  # importamos la librería para generar números aleatorios

# 1. Generar número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# 2. Inicializar contador de intentos
intentos = 0

print("🎲 Bienvenido al juego: Adivina el número")
print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!\n")

# 3. Bucle hasta que el usuario acierte
while True:
    intento = int(input("Ingresa un número: "))  # el jugador propone un número
    intentos += 1  # sumamos un intento

    if intento < numero_secreto:
        print("El número es mayor 📈")
    elif intento > numero_secreto:
        print("El número es menor 📉")
    else:
        print(f"🎉 ¡Correcto! El número era {numero_secreto}")
        print(f"Lo lograste en {intentos} intentos 👏")
        break  # salir del bucle al adivinar
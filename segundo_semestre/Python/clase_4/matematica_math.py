# Sacar la raíz cuadrada de un número positivo

import math

numero = int(input("Ingrese un número positivo: "))

while numero < 0:
    print("Error: El número debe ser positivo.")
    numero = int(input("Ingrese un número positivo: "))

print(f"La raíz cuadrada de {numero} es {math.sqrt(numero)}")


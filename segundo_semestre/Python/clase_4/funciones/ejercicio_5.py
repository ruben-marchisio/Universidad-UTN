# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

# 1. Pedir al usuario un número
num = int(input("Ingrese un número positivo: "))

# 2. Validar que sea positivo
if num < 0:
    print("Error: el número debe ser positivo.")
else:
    # 3. Calcular el factorial usando un bucle
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i   # equivalente a factorial = factorial * i

    # 4. Mostrar el resultado
    print(f"El factorial de {num} es: {factorial}")
#calcular el factorial de un número mayor o igual a 0
# Solicitar al usuario que ingrese un número
num = int(input("Digite un número (mayor o igual a 0): "))

# Verificar que el número sea válido
if num < 0:
    print("El número debe ser mayor o igual a 0.")
else:
    # Inicializar las variables
    i = 1
    factorial = 1
    
    # Calcular el factorial usando un bucle while
    while i <= num:
        factorial = factorial * i
        i = i + 1
    
    # Mostrar el resultado
    print(f"El factorial de {num} es: {factorial}")
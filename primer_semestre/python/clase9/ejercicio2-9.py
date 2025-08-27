#calcular la suma de "N" primeros numeros en python

# Pedir al usuario la cantidad de números a sumarse
N = int(input("Digite la cantidad de números a sumarse: "))

# Inicializar la variable suma en 0
suma = 0

# Sumar desde 1 hasta N
for i in range(1, N + 1):
    suma = suma + i

# Mostrar el resultado
print("La suma es:", suma)

# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#       suma de números pares del 2 al 30
#       suma = 240

# 1. Definimos el rango
inicio = 2
fin = 30

# 2. Creamos una variable acumuladora para la suma
suma = 0

# 3. Recorremos el rango con un bucle for
for numero in range(inicio, fin + 1):  # +1 porque el final no se incluye
    if numero % 2 == 0:  # condición: si es par
        suma += numero   # acumulamos el valor en "suma"

# 4. Mostramos el resultado
print(f"Suma de números pares del {inicio} al {fin} = {suma}")

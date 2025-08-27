#Recorrer un rango de 0 a 10 y mostrar los números que sean divisibles por 3.

for numero in range(0, 11):  # Del 0 al 10
    if numero % 3 == 0:      # Si numero % 3 == 0 significa que no sobra nada, entonces es divisible por 3.
        print(numero)
        
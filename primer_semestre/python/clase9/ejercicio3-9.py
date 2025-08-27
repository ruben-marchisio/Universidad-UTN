#leer 10 numeros e imprimir cuantos son positivos, negativos y cuantos neutros en python

# Inicializar los contadores en 0
conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

# Leer 10 números
for i in range(1, 11):
    num = int(input(f'Digite el número {i}: '))
    
    # Verificar si el número es positivo, negativo o neutro
    if num > 0:
        conteo_positivos += 1
    elif num < 0:
        conteo_negativos += 1
    else:
        conteo_neutros += 1

# Imprimir los resultados
print("Cantidad de números positivos:", conteo_positivos)
print("Cantidad de números negativos:", conteo_negativos)
print("Cantidad de números neutros:", conteo_neutros)

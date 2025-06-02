#supongamos que se tiene un conjunto de calificaciones de un grupo de 10 estudiantes.add
#realizar un algoritmo para calcular la claificacion promedio y la calificacion mas baja del todo el grupo. python

# Inicializar la suma en 0 y la calificación más baja en un valor muy alto
suma = 0
calificacion_baja = float('inf')  # "infinito", así cualquier calificación será menor

# Leer 10 calificaciones
for i in range(1, 11):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    suma += calificacion

    # Actualizar la calificación más baja si corresponde
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

# Calcular el promedio
calificacion_promedio = suma / 10

# Mostrar los resultados
print("La calificación promedio es:", calificacion_promedio)
print("La calificación más baja es:", calificacion_baja)

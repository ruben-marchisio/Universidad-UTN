#Ejercicio 1: Califica tu día 
#¿Cómo estuvo tu día (1 al 10)?
#Mi día estuvo de: 10
#Hacer el código

# Mensaje inicial para dar la bienvenida al usuario
print("Hola, bienvenido a la calificación de tu día")

# Solicita el nombre del usuario y lo guarda en la variable 'nombre'
nombre = input("Ingrese su nombre: ")

# Muestra un saludo personalizado utilizando el nombre ingresado
print("Hola", nombre, "¿Cómo estuvo tu día (1 al 10)?") 

# Solicita una calificación numérica del día y la convierte a un entero
valoracion = int(input("Mi día estuvo de: "))

# Condicional que evalúa la calificación del día y da una respuesta según el rango
if valoracion >= 7:
    # Si la calificación es 7 o superior
    print("Me alegra que tu día haya sido bueno")
elif valoracion >= 4:
    # Si la calificación está entre 4 y 6 (incluido)
    print("Espero que tu día mejore")
else:
    # Si la calificación es menor que 4
    print("Lamento que tu día haya sido malo")

# Mensaje final agradeciendo al usuario por participar
print("Gracias por participar")

# Despedida personalizada utilizando el nombre del usuario
print("Hasta luego", nombre)
    
# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viceversa.
# Investigar las formulas

# 1. Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 2. Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 3. Probar las funciones con ejemplos
print("Ejemplos de conversión:")
print("25°C ->", celsius_a_fahrenheit(25), "°F")
print("100°C ->", celsius_a_fahrenheit(100), "°F")

print("77°F ->", fahrenheit_a_celsius(77), "°C")
print("32°F ->", fahrenheit_a_celsius(32), "°C")

"""
Ejercicio: Determinar si es mayor de edad

Pedir un número al usuario
Almacenar el valor en una variable
Usar la estructura ‘if else’
La formula es: <num> >= 18
True: Eres mayor de edad, Imprimir
False: Eres menor de edad, Imprimir
"""
# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
# Verificar si la edad es mayor o igual a 18
if edad >= 18:
    # Si la condición es verdadera, el usuario es mayor de edad
    print(f"Eres mayor de edad, tienes {edad} años.")
else:
    # Si la condición es falsa, el usuario es menor de edad
    print(f"Eres menor de edad, tienes {edad} años.")
    

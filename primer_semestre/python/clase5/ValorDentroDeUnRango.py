# 1 pedimos al usuario un valor numerico
# 2 verificar si el valor ingresado se encuentra etre el rango de 0 a 5
# 3 la formula es: <num> >= 0 and <num> <= 5

#forma corta de escribir el rango
numero = int(input("Ingrese un numero: "))
if numero >= 0 and numero <= 5:
    print("El numero se encuentra dentro del rango")
else:
    print("El numero no se encuentra dentro del rango")
# 4 si el numero es menor a 0 o mayor a 5, entonces no se encuentra dentro del rango

#forma larga de escribir el rango

valor = int(input("Ingrese un valor: "))
valorMinimo = 0
valorMaximo = 5
dentroDelRango = (valor >= valorMinimo and valor <= valorMaximo) # operador logico and

if dentroDelRango:
    print(f"El valor {valor} se encuentra dentro del rango")
else:
    print(f"El valor {valor} no se encuentra dentro del rango")  
    
    


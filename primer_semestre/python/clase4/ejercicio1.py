#Ejercicio: Número par o impar

#Solicitamos que el usuario ingrese un número
#Este se asigna a una variable
#Utilizaremos la estructura ‘if else’
#La formula: <num> % 2 == 0 Esta operación nos dice si es un número par
#Si es True imprimimos que es par
#Si es False imprimimos que es impar

usuario = int(input("Ingrese un numero: "))
if usuario % 2 == 0:
    # Si el residuo de la división entre 2 es 0, el número es par
    print(f"El numero {usuario} es par")
else:
    # Si el residuo de la división entre 2 no es 0, el número es impar
    print(f"El numero {usuario} es impar")
    

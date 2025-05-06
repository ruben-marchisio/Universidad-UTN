# rango entre 20 y 30 años
# 1 pedir la edad al usuario
# 2 si la edad esta dentro de los 20 a 30 años esta dentro del rango
# 3 combinamos los operadores logicos and y or para saber si el usuario esta dentro del rango o no

edad = int(input("Ingrese su edad: "))

veinte = edad >= 20 and edad < 30
print(veinte) # True si la edad es mayor o igual a 20 y menor a 30

treinta = edad >= 30 and edad < 40
print(treinta) # True si la edad es mayor o igual a 30 y menor a 40

# hacemos la comparacion de los dos rangos con el operador or
if veinte or treinta:
    print("La edad se encuentra dentro del rango (20'0) a (30'0) años")
else:
    print("La edad no se encuentra dentro del rango (20'0) a (30'0) años")

# tambien podemos usar una siintaxis diferente para hacer la comparacion
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("La edad se encuentra dentro del rango (20'0) a (30'0) años")
else:
    print("La edad no se encuentra dentro del rango (20'0) a (30'0) años")

# podemos simplificar del pererador and 

if (20 <= edad < 30) or (30 <= edad < 40):
    print("La edad se encuentra dentro del rango (20'0) a (30'0) años")
else:
    print("La edad no se encuentra dentro del rango (20'0) a (30'0) años")
    
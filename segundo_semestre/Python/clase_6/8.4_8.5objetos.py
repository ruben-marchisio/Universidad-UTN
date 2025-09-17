# 8.4 Creamos más objetos en una clase
# 8.5 Referencias de memoria de objetos con el Debug


class Persona:
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

Persona1 = Persona("Ruben", "Gonzalez", 30)
Persona2 = Persona("Ana", "Lopez", 25)

print(f"el objeto de la clase persona1 es: {Persona1.nombre} {Persona1.apellido} y tiene: {Persona1.edad} años")
print(f"el objeto de la clase persona2 es: {Persona2.nombre} {Persona2.apellido} y tiene: {Persona2.edad} años")

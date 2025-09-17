# 8.6 Modificar atributos de un objeto

class Persona:
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

Persona1 = Persona("Ruben", "Gonzalez", 30) # necesita argumentos

Persona1.nombre = "pedro"
Persona1.apellido = "marchisio"
Persona1.edad = 25

print(f"el objeto1 modificado {Persona1.nombre} {Persona1.apellido} su edad {Persona1.edad}")
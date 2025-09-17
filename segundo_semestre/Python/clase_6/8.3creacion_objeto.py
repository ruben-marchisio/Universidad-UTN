# 8.3 Creación de objetos con argumentos

class Persona:
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

Persona1 = Persona("Ruben", "Gonzalez", 30) # necesita argumentos
Persona2 = Persona("Ana", "Lopez", 25) # necesita argumentos
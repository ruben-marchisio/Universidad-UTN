# 8.8 Métodos de instancia: Definimos un método

class Persona:
    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")
# 14.6 Ejercicio Contador 
# 14.7 Mejoras en el ejercicio Contador

class persona:
    contador_personas = 0
    
    @staticmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __init__(self, nombre, edad):
        persona.contador_personas += 1
        self.id_persona = persona.contador_personas
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"persona[id_persona={self.id_persona}, nombre={self.nombre}, edad={self.edad}]"
    

persona1 = persona("Juan", 30)
print(persona1)
persona2 = persona("Ana", 25)
print(persona2)
persona.generar_siguiente_valor()
persona3 = persona("Luis", 40)
print(persona3)
print(f"Cantidad de personas: {persona.contador_personas}")


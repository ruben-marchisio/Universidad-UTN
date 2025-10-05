# 10.1 Métodos: setter and getter parte 1 y 2
# 10.2 Atributos read-only (solo lectura)

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"La clase Persona tiene los siguientes atributos: {self._nombre} {self._apellido} {self._edad}")
    
    
    # Getter
    @property # Decorador
    def nombre(self):
        print("Estamos utilizando el método get")
        return self._nombre
    
    # Setter
    @nombre.setter # Decorador
    def nombre(self, nombre):
        print("Estamos utilizando el método set")
        self._nombre = nombre
    @property # Decorador
    def apellido(self):
        return self._apellido
    @apellido.setter # Decorador
    def apellido(self, apellido):
        self._apellido = apellido
    @property # Decorador
    def edad(self):
        return self._edad
    # No definimos el setter para que sea un atributo de solo lectura (read-only)
    
    def __del__(self):
        print(f"Se elimina el objeto: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":
    # Bloque principal
    Persona1 = Persona("Juan", "Perez", 30)
    print(Persona1.nombre) # Llamamos al método get
    Persona1.nombre = "Juan Carlos" # Llamamos al método set
    print (Persona1.nombre) # Llamamos al método get
    print(Persona1.mostrar_detalle()) # Llamamos al método mostrar detalle

    # atributo de solo lectura read-only por no tener el método set
    print(Persona1.edad)

    print(__name__) # Nos indica el módulo en ejecución
    


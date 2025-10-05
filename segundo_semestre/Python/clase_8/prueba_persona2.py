# 10.4 Uso de clases y módulos
# 10.5 Comprobación del módulo principal en ejecución
# 10.6 Destructor de objetos
from persona2 import Persona
print("Creando el objeto".center(30, "-"))
if __name__ == "__main__":
    # Bloque principal
    Persona1 = Persona("Pedro", "gonzalo", 30)

    Persona1.mostrar_detalle()

    print(__name__) # Nos indica el módulo en ejecución
    

print("Eliminamos el objeto".center(30, "-"))
del Persona1 # esto no es necesario hacerlo, python lo hace automáticamente
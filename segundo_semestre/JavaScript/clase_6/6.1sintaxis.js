// 6.1 Sintaxis de Clases en JavaScript: Parte 1 y 2


// Definición de una clase (plantilla para crear objetos)
class Persona {
    // El constructor es un método especial que se ejecuta
    // automáticamente al crear una nueva instancia de la clase.
    constructor(nombre, apellido) {
        // "this" hace referencia al objeto actual.
        // Guardamos los valores en propiedades internas.
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

// Crear un objeto (instancia) de la clase Persona
let persona1 = new Persona("Carlos", "Gómez");
console.log(persona1); 
// Salida: Persona { nombre: 'Carlos', apellido: 'Gómez' }

// Crear otro objeto con distintos valores
let persona2 = new Persona("Juli", "Martínez");
console.log(persona2); 
// Salida: Persona { nombre: 'Juli', apellido: 'Martínez' }


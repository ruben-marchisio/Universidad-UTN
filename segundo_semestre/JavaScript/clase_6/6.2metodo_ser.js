// 6.2 Método Get y Set: Parte Get y Parte Set

class Persona {
    constructor(nombre, apellido) {
        // Convención: usar "_" delante del nombre indica propiedad "privada"
        // (no es realmente privada, pero es una práctica común)
        this._nombre = nombre;
        this._apellido = apellido;
    }

    // 🔹 Getter → permite obtener el valor como si fuera una propiedad
    get nombre() {
        return this._nombre;
    }

    // 🔹 Setter → permite asignar un nuevo valor de forma controlada
    set nombre(nombre) {
        this._nombre = nombre;
    }
}

// Crear una instancia de la clase Persona
let persona1 = new Persona("Pepe", "Gómez");

// Usando el getter (accede como si fuera una propiedad)
console.log(persona1.nombre); // salida: Pepe

// Usando el setter (modifica el valor interno de _nombre)
persona1.nombre = "Rubén";

// Volvemos a usar el getter para ver el cambio
console.log(persona1.nombre); // salida: Rubén


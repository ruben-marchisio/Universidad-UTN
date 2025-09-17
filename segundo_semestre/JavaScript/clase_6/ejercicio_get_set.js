// Crear el método get y set para el atributo de apellido, luego modificar 
// el apellido a través del  set y mostrar con un console.log lo que es
//  el get donde muestra el resultado obtenido.

//  Clase Persona con getters y setters para nombre y apellido
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    // Getter y Setter para nombre
    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    //  Getter y Setter para apellido
    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }
}

// Crear una instancia
let persona1 = new Persona("Pepe", "Gómez");

//  Modificar el apellido con el setter
persona1.apellido = "Martínez";

//  Mostrar el apellido actualizado con el getter
console.log("Apellido actualizado:", persona1.apellido); 
// salida: Apellido actualizado: Martínez


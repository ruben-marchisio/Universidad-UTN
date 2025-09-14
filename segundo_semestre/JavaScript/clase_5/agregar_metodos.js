//5.3 Agregar métodos al constructor del objeto

function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function() { // método agregado al constructor
        return this.nombre + " " + this.apellido;
    }
}

let padre = new Persona("Juan", "Perez", "pere@gmail.com");
console.log(padre);
console.log(padre.nombreCompleto()); // llamamos al método del objeto

let madre = new Persona("Laura", "Quinteros", "pepe@gmail.com  ");
console.log(madre);
console.log(madre.nombreCompleto()); // llamamos al método del objeto
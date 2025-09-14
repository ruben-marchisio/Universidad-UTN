//5.2 Constructores de objetos

function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    }

let padre = new Persona("Juan", "Perez", "juan@gmail.com");
// se puede modificar el objeto
padre.nombre = "Carlos";
padre.apellido = "Lara";
console.log(padre);
console.log(padre.nombre);
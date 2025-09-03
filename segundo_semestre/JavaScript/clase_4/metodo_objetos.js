//1.2 Agregamos métodos a los Objetos

let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "juan@gmail.com",
    edad : 28,
    nombreCompleto: function(){  //método
        return this.nombre + ' ' + this.apellido
    }
}

console.log(persona.nombreCompleto()) //método

;


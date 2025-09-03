//1.5 Agregar y eliminar propiedades de los Objetos

let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "juan@gmail.com",
}

console.log(persona);

// Agregar una propiedad
persona.edad = 28
console.log(persona);

//modificar una propiedad
persona.email = "perezjuan@gmail.com"
console.log(persona);

//eliminar una propiedad
delete persona.apellido
console.log(persona);

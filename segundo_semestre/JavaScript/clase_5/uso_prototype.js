// 5.5 El uso de prototype

function Persona(nombre, apellido, edad){
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;

}
Persona.prototype.telefono = "123456789"; //Agregamos una propiedad al prototipo de Persona

console.log(Persona.prototype); //Mostramos el prototipo de Persona

// modificamos el numero de telefono del prototipo
Persona.prototype.telefono = "987654321";

let persona1 = new Persona("Juan", "Perez", 30);
let persona2 = new Persona("Maria", "Gomez", 25);

console.log(persona1);
console.log(persona2);

console.log(persona1.telefono); //Accedemos a la propiedad telefono del prototipo
console.log(persona2.telefono); //Accedemos a la propiedad telefono del prototipo


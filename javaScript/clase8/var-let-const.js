// aplicando el uso de var, let y const

/*
con var podes reasignar en cualquier momento este forma parte del ambito 
global.
un error es que se sobreescriba 
EJemplo:
*/

var nombre = "pepe";
var nombre = "juan"; // se puede reasignar
console.log(nombre); // "juan"
// con let no se puede reasignar, es de ambito local

function saludar() {
    var nombre2 = "pepe";

    console.log(nombre2); // "pepe"
}

//console.log(nombre2); // esto no funcionará, ya que nombre2 es local a la función saludar lo cual no se puede acceder desde fuera de la función

// pero que pasa con if, for, while, etc.?

if (true) {
    var edad = 30;
    console.log(edad);
}

console.log(edad); // esto funcionará, ya que var es de ámbito global puede ser un error si se usa mal
// con let no se puede reasignar, es de ambito local por lo que no se puede acceder desde fuera del bloque y es mejor usarlo para evitar errores

if (true) {
    let edad2 = 30;
    console.log(edad2); // esto funcionará, ya que edad2 es local al bloque if
}

// console.log(edad2); // esto no funcionará, ya que edad2 es local al bloque if lo cual no se puede acceder desde fuera del bloque

/* 
const es una constante, no se puede reasignar, es de ambito local y no se puede modificar su valor una vez asignado
si se intenta reasignar, se producirá un error
ejemplo:
*/ 

 const dni = 3648689;
// dni = 12345678; // esto producirá un error, ya que no se puede reasignar una constante
console.log(dni); // 3648689
// const dni2; // esto producirá un error, ya que no se puede declarar una constante sin asignarle un valor

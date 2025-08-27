//tipos de datos booleanos

var bandera = true; //true o false
console.log(bandera);

console.log(typeof bandera);

//tipo de dato funcion

function mifuncion() {} //es una funcion vacia
console.log(typeof mifuncion);

//tipo de dato simbolo
//es un tipo de dato que se utiliza para crear identificadores unicos

var simbolo = Symbol("mi simbolo");
console.log(typeof simbolo); //es un tipo de dato simbolo

//tipos de dato clase

class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

console.log(typeof Persona); //es un tipo de dato clase

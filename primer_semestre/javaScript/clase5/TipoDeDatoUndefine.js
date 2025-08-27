// Tipo de Dato Undefined 

// En JavaScript, el tipo de dato undefined es un tipo primitivo que representa la ausencia de valor o la falta de definición de una variable.
// Una variable que ha sido declarada pero no inicializada tiene el valor undefined.

var x; // Declaramos una variable sin inicializarla
console.log(x); // Imprime undefined, ya que x no tiene un valor asignado
console.log(typeof x); // Imprime "undefined", que es el tipo de dato de x

//null es un valor asignado a una variable que representa la ausencia intencionada de cualquier objeto o valor.
var y = null; 
console.log(y); // Imprime null, ya que y tiene el valor null
console.log(typeof y); // Imprime "object", que es el tipo de dato de y, aunque esto es un error en JavaScript

// Declaramos una función de tipo EXPRESIÓN
// En lugar de usar "function nombre()", la guardamos dentro de una variable.
// Importante: termina con punto y coma (;) porque es una asignación.

let sumar = function (a, b) {
  return a + b;
}; 

//  Para usarla, llamamos a la variable como si fuera una función
let resultado = sumar(5, 2);

// 🔹Mostramos el resultado en consola
console.log(resultado);
// Paso por valor
// En JavaScript, los TIPOS PRIMITIVOS (number, string, boolean, null, undefined, symbol, bigint)
// se pasan a las funciones por VALOR, no por referencia.

let x = 10; // variable con un número (tipo primitivo)

function cambiarValor(a) {
    // "a" recibe una COPIA del valor de x
    a = 20; // solo cambia la copia interna, NO la variable original
    console.log("Dentro de la función a:", a); // salida: 20
}

// Llamamos a la función pasando x
cambiarValor(x);

console.log("Fuera de la función x:", x); // salida: 10

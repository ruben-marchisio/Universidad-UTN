// Una función sirve para reutilizar código y organizar mejor el programa.
// Se puede llamar (usar) varias veces sin tener que escribir el mismo código de nuevo.


// IMPORTANTE: en JavaScript las funciones declaradas con "function" 
// se pueden llamar ANTES o DESPUÉS de ser declaradas (hoisting).

// Ejemplo: llamamos la función antes de escribirla
miFuncion(5, 4); 

// Declaración de la función
function miFuncion(a, b) {
  console.log("sumamos: " + (a + b)); // se ejecuta cada vez que llamamos la función
}

// Llamando nuevamente a la función (ahora después de declararla)
miFuncion(2, 3); 



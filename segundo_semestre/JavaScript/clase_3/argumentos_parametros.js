// Argumentos y parámetros en funciones
// Parámetros → variables que definimos en la función (a, b)
// Argumentos → valores reales que pasamos al llamar la función

let sumar = function(a, b) {
    // El objeto "arguments" contiene TODOS los valores pasados a la función,
    // aunque no estén definidos como parámetros.
    
    console.log("Primer argumento (a):", arguments[0]); // muestra 3
    console.log("Segundo argumento (b):", arguments[1]); // muestra 7
    console.log("Tercer argumento extra:", arguments[2]); // muestra 5

    // La función suma los dos parámetros y también el argumento extra
    return a + b + arguments[2]; 
};

// Al llamar la función, pasamos 3 argumentos (3, 7, 5)
let resultado = sumar(3, 7, 5);

// Mostramos el valor devuelto
console.log("Resultado final:", resultado); // salida: 15
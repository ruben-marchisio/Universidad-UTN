// Crear un array vacío para almacenar los números aleatorios
let numeros = [];
// Generar 10 números aleatorios entre 1 y 100
for (let i = 0; i < 10; i++) {
    // Math.random() genera un número decimal entre 0 y 1
    // Multiplicamos por 100 para tener un rango de 0 a 99.999...
    // Math.floor() redondea hacia abajo al entero más cercano
    // Sumamos 1 para obtener números del 1 al 100 (incluyendo ambos)
    numeros.push(Math.floor(Math.random() * 100) + 1);
}
// Mostrar por consola los números generados aleatoriamente
console.log("Números generados: ", numeros);
// Crear arrays vacíos para pares e impares
let pares = [];
let impares = [];
// Recorrer el array de números para clasificarlos en pares e impares
for (let i = 0; i < numeros.length; i++) {
    // Usamos el operador módulo (%) para saber si un número es par o impar
    // Si el resto de la división por 2 es 0, es par; si no, es impar
    if (numeros[i] % 2 === 0) {
        pares.push(numeros[i]);     // Agregamos el número al array de pares
    } else {
        impares.push(numeros[i]);   // Agregamos el número al array de impares
    }
}
// Mostrar los números pares encontrados
console.log("Números pares: ", pares);

// Mostrar los números impares encontrados
console.log("Números impares: ", impares);


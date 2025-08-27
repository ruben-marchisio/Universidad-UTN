// convertir string a número
let numero = "5";
console.log(typeof numero); // "string"
let edad = Number(numero);
console.log(typeof edad); // "number"

// si la edad es mayor o igual a 18

if (edad >= 18) {
    console.log("La persona es mayor de edad");
}   
else {
    console.log("La persona es menor de edad");
}

// ternario
let resultado = (edad >= 18) ? "La persona es mayor de edad" : "La persona es menor de edad";

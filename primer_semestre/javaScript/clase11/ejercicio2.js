//Usando switch

let mes = 4;

switch (mes) {
    case 1:
        console.log("Enero");
        break;
    case 2:
        console.log("Febrero");
        break;
    case 3:
        console.log("Marzo");
        break;
    case 4:
        console.log("Abril");
        break;
    case 5:
        console.log("Mayo");
        break;
    case 6:
        console.log("Junio");
        break;
    case 7:
        console.log("Julio");
        break;
    case 8:
        console.log("Agosto");
        break;
    case 9:
        console.log("Septiembre");
        break;
    case 10:
        console.log("Octubre");
        break;
    case 11:
        console.log("Noviembre");
        break;
    case 12:
        console.log("Diciembre");
        break;
    default:
        console.log("No es un mes válido");
}

// Mejorada usando array y función
const meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
];

function mostrarMes(numeroMes) {
    if (numeroMes >= 1 && numeroMes <= 12) {
        console.log(meses[numeroMes - 1]);
    } else {
        console.log("No es un mes válido");
    }
}

// Ejemplos de uso:
mostrarMes(4);  // Abril
mostrarMes(11); // Noviembre
mostrarMes(13); // No es un mes válido


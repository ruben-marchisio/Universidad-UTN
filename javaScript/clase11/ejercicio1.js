//Evitar repetir tu codigo

let dias = 1;
switch (dias) {
    case 1:
        console.log("Hoy es Lunes");
        break;
    case 2:
        console.log("Hoy es Martes");
        break;
    case 3: 
        console.log("Hoy es Miercoles");
        break;
    case 4:
        console.log("Hoy es Jueves");
        break;
    case 5:
        console.log("Hoy es Viernes");
        break;
    case 6:
        console.log("Hoy es Sabado");
        break;
    case 7:
        console.log("Hoy es Domingo");
        break;
        console.log("No es un dia de la semana");
        break;
}

// opcion mejorada

const diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];

function mostrarDia(dia) {  
    if (dia >= 1 && dia <= 7) {
        console.log(`Hoy es ${diasSemana[dia - 1]}`);
    } else {
        console.log("No es un día de la semana");
    }
}

// Ejemplos de uso:
mostrarDia(1); // Hoy es Lunes
mostrarDia(5); // Hoy es Viernes
mostrarDia(9); // No es un día de la semana
//Estructura switch con el break

// Número de mes asignado directamente
let mes = 4; // Cambia este valor para probar otros meses

let estacion = "";

switch (mes) {
  case 12:
  case 1:
  case 2:
    estacion = "Verano";
    break;
  case 3:
  case 4:
  case 5:
    estacion = "Otoño";
    break;
  case 6:
  case 7:
  case 8:
    estacion = "Invierno";
    break;
  case 9:
  case 10:
  case 11:
    estacion = "Primavera";
    break;
  default:
    estacion = "Mes inválido";
    break;
}

console.log("La estación del año es: " + estacion);

// Asignar directamente la hora (formato 24 horas)
let hora = 17; // Cambia este valor para probar

let mensaje = "";

switch (hora) {
  case 6:
  case 7:
  case 8:
  case 9:
  case 10:
  case 11:
    mensaje = "Es de mañana";
    break;
  case 12:
  case 13:
  case 14:
  case 15:
  case 16:
  case 17:
  case 18:
    mensaje = "Es de tarde";
    break;
  case 19:
  case 20:
  case 21:
  case 22:
  case 23:
  case 0:
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
    mensaje = "Es de noche";
    break;
  default:
    mensaje = "Hora inválida";
    break;
}

console.log(mensaje);

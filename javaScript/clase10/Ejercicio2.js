//Hora del día

// Asigna directamente la hora (en formato 24 horas)
let hora = 17; // Cambia este valor para probar

let mensaje = '';

// Determina el momento del día según la hora
if (hora >= 6 && hora < 12) {
  mensaje = 'Es de mañana';
} else if (hora >= 12 && hora < 19) {
  mensaje = 'Es de tarde';
} else if ((hora >= 19 && hora <= 23) || (hora >= 0 && hora < 6)) {
  mensaje = 'Es de noche';
} else {
  mensaje = 'Hora inválida';
}

// Muestra el resultado
console.log(mensaje);

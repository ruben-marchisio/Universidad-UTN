// Calcular estación del año

// Asignar directamente el número del mes a la variable
let mes = 8; // Cambia este valor para probar otros meses

let estacion = '';

// Determinar la estación del año según el número de mes (hemisferio sur)
if (mes === 12 || mes === 1 || mes === 2) {
  estacion = 'Verano';
} else if (mes === 3 || mes === 4 || mes === 5) {
  estacion = 'Otoño';
} else if (mes === 6 || mes === 7 || mes === 8) {
  estacion = 'Invierno';
} else if (mes === 9 || mes === 10 || mes === 11) {
  estacion = 'Primavera';
} else {
  estacion = 'Mes inválido';
}

// Mostrar el resultado
console.log('La estación del año es: ' + estacion);




// Tipos de datos en una función

function miFuncion(a, b) {
  console.log(arguments);
  console.log(arguments.length);
}

miFuncion(1, 2, 3, 4, 5, 6);

//tostring 
let miFuncionTexto = miFuncion.toString();
console.log(miFuncionTexto);
//Funciones de tipo self y invoking
// Son funciones que se ejecutan automáticamente al ser definidas.
// No necesitan ser llamadas explícitamente.
// no la podemos reutilizar, solo se ejecuta una vez.

(function(a, b) {
  console.log("ejecutando la función: " + (a + b));
})(9, 6); // Pasamos los argumentos directamente al final de la función



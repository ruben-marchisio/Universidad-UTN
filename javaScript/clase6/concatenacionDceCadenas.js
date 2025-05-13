let nombre = "Juan";
let apellido = "Pérez";
var nombreCompleto = nombre + " " + apellido;   
console.log(nombreCompleto); // Juan Pérez
// Concatenación de cadenas con el operador +

var nombreCompleto2 = "Ruben" + " " + "marcchisio";
console.log(nombreCompleto2); 

var juntos = nombre + 219
console.log(juntos); // Juan219

juntos = nombre + 2 + 19 // estono es una concatenacion lo que no significa que no va a realizar una operacion matematica
console.log(juntos); // Juan219

juntos = 2 + 19 + nombre // al estar al principio de la cadena se va a realizar la suma por lo que el resultado va a ser 21
console.log(juntos); // esto es porque lo primero que se encuentra es un numero y luego es string
// por lo que se va a realizar la suma

//otra forma de concatenar y suymar es con () ya que se va a realizar primero la suma y luego la concatenacion
juntos = nombre + (2 + 19) // al estar entre parentesis se va a realizar primero la suma y luego la concatenacion por regla de precedencia
console.log(juntos); // Juan21

//usando el operador simplificado

nombre += " " + apellido; // nombre = nombre + " " + apellido

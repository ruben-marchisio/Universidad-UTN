//paso por referencia

const persona = {
    nombre: "Juan",
    apellido: "Pérez",
    edad: 30
};

function cambiarValor(p1){
    p1.nombre = "Carlos"; // Modifica la propiedad del objeto
    p1.edad = 35; // Modifica otra propiedad del objeto
    console.log("Dentro de la función p1:", p1);

}
// Llamamos a la función pasando el objeto persona
cambiarValor(persona);
console.log("Fuera de la función persona:", persona);


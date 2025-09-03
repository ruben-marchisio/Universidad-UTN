//1.3 Diferentes formas de crear un Objeto
//1.4 Cómo acceder a las propiedades de los Objetos

let persona1 = new Object() //forma 1
persona1.nombre = "Juan"
persona1.apellido = "Perez"
persona1.edad = 28
persona1.telefono = "12345678"

console.log(persona1);
console.log(persona1.nombre);

console.log(persona1['apellido']); 

// for in y acceder al objeto como si fuera un arreglo
for (propiedad in persona1){
    console.log(propiedad);
    console.log(persona1[propiedad]);
}

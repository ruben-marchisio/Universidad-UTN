// 5.1 Métodos get y set Parte 1 y 2


let persona = {
    nombre: "Juan",
    apellido: "Perez",
    edad: 28,
    idioma: "es",
    get lang() {
        return this.idioma.toUpperCase(); // convierte a mayusculas
    },
    set lang(lang) {
        this.idioma = lang.toUpperCase(); //
    },
    get getNombre() {
        return "EL NOMBRE: " + this.nombre + " " + "edad: " + this.edad;
    }
}

console.log(persona.getNombre);
console.log(persona.lang); // accedemos como si fuera un atributo
persona.lang = "en";
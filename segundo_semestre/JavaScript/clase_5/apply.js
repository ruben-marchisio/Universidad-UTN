// 5.7 El uso de apply

let persona = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto: function(){
        return this.nombre + " " + this.apellido; 
    }
}

let persona2 = {
    nombre: "Carlos",
    apellido: "Lara"
}
console.log(persona.nombreCompleto.apply(persona2 )); //Carlos Lar


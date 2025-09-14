// 5.6 El uso de call

let persona = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto: function(titulo, telefono){
        return titulo + ": " + this.nombre + " " + this.apellido + ", " + telefono;
    }
}

let persona2 = {
    nombre: "Carlos",
    apellido: "Lara"
}

//Uso de call para usar el metodo nombreCompleto de persona en el objeto persona2
console.log(persona.nombreCompleto("Ing", "123456789")); //Ing: Juan Perez, 123456789
console.log(persona.nombreCompleto.call(persona2, "Lic", "987654321")); //Lic: Carlos Lara, 987654321

// 6.3 hoisting y clases: Parte 1 y 2

// let persona1 = new Persona("Pepe", "Gómez"); esto no se hace nunca antes de la clase 

class persona {
  constructor(nombre, apellido) {
    this._nombre = nombre;
    this._apellido = apellido;
  }
  get nombre() {
    return this._nombre;
  }
  set nombre(nombre) {
    this._nombre = nombre;
  }
}

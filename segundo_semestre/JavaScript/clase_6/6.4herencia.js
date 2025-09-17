// Clase Padre
class Persona {
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

// Clase Hija que hereda de Persona
class Empleado extends Persona {
  constructor(nombre, apellido, departamento) {
    // "super" llama al constructor de la clase padre (Persona)
    super(nombre, apellido);
    this._departamento = departamento;
  }

  get departamento() {
    return this._departamento;
  }

  set departamento(departamento) {
    this._departamento = departamento;
  }
}

// Crear una instancia de la clase hija
let empleado1 = new Empleado("María", "Sir", "Control");

// Ver el objeto completo
console.log(empleado1);

// Acceder a valores con getters
console.log("Nombre:", empleado1.nombre);       // salida: María
console.log("Departamento:", empleado1.departamento); // salida: Control
package javaa.clase_4;

public class prueba_persona {
    public static void main(String[] args) {
        persona persona1;
        persona1 = new persona();
        persona1.nombre = "Ruben";
        persona1.apellido = "Gonzalez";
        persona1.obtenerInformacion();

        // creamos otro objeto
        persona persona2 = new persona();
        System.out.println("Persona 2 = " + persona2);
        System.out.println("Nombre persona 1 = " + persona1.nombre);
        persona2.obtenerInformacion();
        persona2.nombre = "Ana";
        persona2.apellido = "Lopez";
        persona2.obtenerInformacion();

    }
    
}

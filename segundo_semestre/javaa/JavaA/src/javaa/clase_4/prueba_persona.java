package javaa.clase_4;

public class prueba_persona {
    public static void main(String[] args) {
        Personaa persona1;
        persona1 = new Personaa();
        persona1.nombre = "Ruben";
        persona1.apellido = "Gonzalez";
        persona1.obtenerInformacion();

        // creamos otro objeto
        Personaa persona2 = new Personaa();
        System.out.println("Persona 2 = " + persona2);
        System.out.println("Nombre persona 1 = " + persona1.nombre);
        persona2.obtenerInformacion();
        persona2.nombre = "Ana";
        persona2.apellido = "Lopez";
        persona2.obtenerInformacion();

    }
    
}

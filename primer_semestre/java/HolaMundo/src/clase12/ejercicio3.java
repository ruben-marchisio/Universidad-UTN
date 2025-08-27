package clase12;


import java.util.Scanner;


public class ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir las calificaciones al usuario
        System.out.print("Ingrese la calificación de Participación (10%): ");
        double participacion = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Primer Examen Parcial (25%): ");
        double primerParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Segundo Examen Parcial (25%): ");
        double segundoParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Examen Final (40%): ");
        double examenFinal = scanner.nextDouble();

        // Calcular la calificación final con las ponderaciones
        double calificacionFinal = 
            (participacion * 0.10) +
            (primerParcial * 0.25) +
            (segundoParcial * 0.25) +
            (examenFinal * 0.40);

        // Mostrar el resultado
        System.out.println("La calificación final del estudiante es: " + calificacionFinal);
    }
 
}

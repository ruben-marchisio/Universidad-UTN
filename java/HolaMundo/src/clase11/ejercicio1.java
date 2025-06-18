
import java.util.Scanner;


public class ejercicio1 {
    public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);

        double nota1, nota2, nota3, promedio;

        // Leer la primera nota y mostrar mensaje
        System.out.print("Ingrese la primera nota: ");
        nota1 = scanner.nextDouble();
        System.out.println("La primera nota es: " + nota1);

        // Leer la segunda nota y mostrar mensaje
        System.out.print("Ingrese la segunda nota: ");
        nota2 = scanner.nextDouble();
        System.out.println("La segunda nota es: " + nota2);

        // Leer la tercera nota y mostrar mensaje
        System.out.print("Ingrese la tercera nota: ");
        nota3 = scanner.nextDouble();
        System.out.println("La tercera nota es: " + nota3);

        // Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3;

        // Mostrar resultado final
        if (promedio >= 70) {
            System.out.println("El alumno está aprobado con promedio: " + promedio);
        } else {
            System.out.println("El alumno está desaprobado con promedio: " + promedio);
        }

        scanner.close();
    }
}

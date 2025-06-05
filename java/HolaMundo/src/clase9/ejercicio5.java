
import java.util.Scanner;


public class ejercicio5 {
    //hacer un programa que calcule e imprima la suma de tres calificaciones
    //pedir las calificaciones al usuario
         public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Pedir tres calificaciones al usuario
        System.out.print("Ingrese la primera calificación: ");
        double cal1 = entrada.nextDouble();

        System.out.print("Ingrese la segunda calificación: ");
        double cal2 = entrada.nextDouble();

        System.out.print("Ingrese la tercera calificación: ");
        double cal3 = entrada.nextDouble();

        // Calcular la suma
        double suma = cal1 + cal2 + cal3;

        // Calcular el promedio
        double promedio = suma / 3;

        // Mostrar los resultados
        System.out.println("La suma de las tres calificaciones es: " + suma);
        System.out.println("El promedio de las tres calificaciones es: " + promedio);

        entrada.close();
    }
}



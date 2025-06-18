
import java.util.Scanner;


public class ejercicio3 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double num1, num2, resultado;

        // Leer los dos números
        System.out.print("Digite el primer número: ");
        num1 = scanner.nextDouble();

        System.out.print("Digite el segundo número: ");
        num2 = scanner.nextDouble();

        // Evaluar las condiciones
        if (num1 == num2) {
            resultado = num1 * num2;
            System.out.println("Son iguales, los multiplicamos.");
        } else if (num1 > num2) {
            resultado = num1 - num2;
            System.out.println("El primero es mayor, los restamos.");
        } else {
            resultado = num1 + num2;
            System.out.println("El primero NO es mayor, los sumamos.");
        }

        // Mostrar el resultado
        System.out.println("El resultado es: " + resultado);

        scanner.close();
    }
 
}

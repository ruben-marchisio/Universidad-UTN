
import java.util.Scanner;


public class ejercicio2 {
    public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);

        double compra, descuento, precioFinal;

        // Pedir la cantidad de la compra
        System.out.print("Digite la cantidad a pagar: ");
        compra = scanner.nextDouble();

        // Calcular descuento
        if (compra > 100) {
            descuento = compra * 0.2; // 20%
        } else {
            descuento = 0;
        }

        // Calcular el precio final
        precioFinal = compra - descuento;

        // Mostrar el precio a pagar
        System.out.println("El precio a pagar es: " + precioFinal);

        scanner.close();
    }
}

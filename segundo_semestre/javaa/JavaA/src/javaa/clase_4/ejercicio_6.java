//Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar la 
//suma de todos los números introducidos.
package javaa.clase_4;

import java.util.Scanner;

public class ejercicio_6 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int numero;
            int suma = 0;

            System.out.println("Ingrese números (0 para terminar):");

            do {
                numero = sc.nextInt(); // leer número
                suma += numero;        // acumular en suma
            } while (numero != 0);     // repetir hasta que se ingrese 0

            System.out.println("La suma de los números introducidos es: " + suma);
        }

    }
}

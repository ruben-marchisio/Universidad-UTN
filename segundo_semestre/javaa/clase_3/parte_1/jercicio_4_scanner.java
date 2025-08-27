// pedir numeros hasta que se ingrese uno negativo
// y mostrar cuantos numeros se ingresaron


// Versión con Scanner
package javaa.clase_3.parte_1;

import java.util.Scanner;

public class jercicio_4_scanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero;          // número ingresado
        int contador = 0;    // cuántos números se introdujeron

        // Pedir el primer número
        System.out.println("Ingrese un número (negativo para salir): ");
        numero = sc.nextInt();

        // Mientras el número no sea negativo
        while (numero >= 0) {
            contador++; // sumamos uno al contador

            // Pedir otro número
            System.out.println("Ingrese otro número (negativo para salir): ");
            numero = sc.nextInt();
        }

        // Al terminar, mostramos cuántos números se ingresaron
        System.out.println("Se introdujeron " + contador + " números.");

        sc.close(); // cerrar el scanner
    }
}

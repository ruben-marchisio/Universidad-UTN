
package javaa.clase_5;

import java.util.Scanner;

public class Ejercicio_8 {


    public static void main(String args[]) {
            // Creamos el objeto Scanner para leer desde teclado
        Scanner sc = new Scanner(System.in);

        // Variable donde guardaremos el número ingresado por el usuario
        int N;

        // Pedimos el número al usuario
        System.out.print("Ingrese un número: ");
        N = sc.nextInt();

        // Bucle for: va desde 1 hasta N
        for (int i = 1; i <= N; i++) {
            System.out.println(i); // mostramos el número actual
        }

        // Cerramos el scanner
        sc.close();
    }
}

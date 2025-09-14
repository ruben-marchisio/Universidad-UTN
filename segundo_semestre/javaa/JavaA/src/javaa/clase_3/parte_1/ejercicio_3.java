// leer numeros hasta que se introduzca un 0
// para cada numero indicar si es par o impar
// primero con la clase Scanner
// luego con JOptionPane

// clase Scanner
package javaa.clase_3.parte_1;

import java.util.Scanner;

public class ejercicio_3 {
    public static void main(String[] args) {
        // Creamos el objeto Scanner para leer desde teclado
        Scanner sc = new Scanner(System.in);
        
        int numero; // variable para almacenar cada número ingresado
        
        // Pedimos el primer número
        System.out.println("Ingrese un número (0 para salir): ");
        numero = sc.nextInt();
        
        // Bucle while: se repite hasta que el usuario ingrese 0
        while (numero != 0) {
            // Verificamos si es par o impar
            if (numero % 2 == 0) {
                System.out.println(numero + " es par.");
            } else {
                System.out.println(numero + " es impar.");
            }
            
            // Pedimos otro número
            System.out.println("Ingrese otro número (0 para salir): ");
            numero = sc.nextInt();
        }
        
        System.out.println("Programa finalizado.");
        sc.close(); // Cerramos el scanner
    }
}

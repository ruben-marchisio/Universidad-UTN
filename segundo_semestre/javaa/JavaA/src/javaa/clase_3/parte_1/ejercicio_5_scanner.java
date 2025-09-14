// realizar un juego para aivinar un numero
// para ello generar un numero aleatorio entrew 0 y 100
// y luego ir pidiendo numeros indicando "es mayor" o "es menor"


//5 Versión con Scanner
package javaa.clase_3.parte_1;

import java.util.Scanner;

public class ejercicio_5_scanner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Generar número aleatorio entre 0 y 100
        int numeroSecreto = (int) (Math.random() * 101);
        int intento;       // número que ingresa el usuario
        int contador = 0;  // cantidad de intentos

        System.out.println("Juego: Adivina el número (entre 0 y 100)");

        // Bucle hasta que el usuario acierte
        do {
            System.out.print("Introduce un número: ");
            intento = sc.nextInt();
            contador++; // aumentamos el contador de intentos

            if (intento < numeroSecreto) {
                System.out.println("El número secreto es MAYOR");
            } else if (intento > numeroSecreto) {
                System.out.println("El número secreto es MENOR");
            } else {
                System.out.println("¡Acertaste! El número era " + numeroSecreto);
                System.out.println("Lo lograste en " + contador + " intentos.");
            }

        } while (intento != numeroSecreto);

        sc.close();
    }
}

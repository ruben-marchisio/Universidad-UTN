
package javaa.clase_5;

import java.util.Scanner;


public class Ejercicio_9 {

    public static void main(String args[]) {
         Scanner sc = new Scanner(System.in);

        // Variables para guardar día, mes y año
        int dia, mes, anio;

        // Pedimos los datos
        System.out.print("Ingrese el día: ");
        dia = sc.nextInt();

        System.out.print("Ingrese el mes: ");
        mes = sc.nextInt();

        System.out.print("Ingrese el año: ");
        anio = sc.nextInt();

        // Validamos la fecha
        if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && anio > 0) {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es correcta.");
        } else {
            System.out.println("La fecha ingresada NO es correcta.");
        }

        sc.close(); 
    }
}

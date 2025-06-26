package clase12;


import java.util.Scanner;


public class ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir el total de horas al usuario
        System.out.print("Ingrese el total de horas: ");
        int totalHoras = scanner.nextInt();

        // 1 semana = 7 días = 7 * 24 = 168 horas
        int semanas = totalHoras / 168;
        int horasRestantes = totalHoras % 168;

        // 1 día = 24 horas
        int dias = horasRestantes / 24;
        int horas = horasRestantes % 24;

        // Mostrar el resultado
        System.out.println(totalHoras + " horas equivalen a:");
        System.out.println(semanas + " semanas, " + dias + " días y " + horas + " horas.");  
    }
}

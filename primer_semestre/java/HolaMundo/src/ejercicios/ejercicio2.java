
import java.util.Scanner;
//Hacer un programa que calcule e imprima el salario de un empleado, a partir de sus horas 
//semanales trabajadas y de su salario por hora.

public class ejercicio2 {
    public static void main(String[] args) {
        // Creamos un objeto Scanner para leer datos desde el teclado
        Scanner entrada = new Scanner(System.in);

        // Pedimos las horas semanales trabajadas
        System.out.print("Ingrese la cantidad de horas trabajadas en la semana: ");
        int horas = entrada.nextInt();

        // Pedimos el salario por hora
        System.out.print("Ingrese el salario por hora: ");
        double salarioHora = entrada.nextDouble();

        // Calculamos el salario total
        double salarioTotal = horas * salarioHora;

        // Mostramos el resultado
        System.out.println("El salario semanal del empleado es: $" + salarioTotal);

        // Cerramos el Scanner
        entrada.close();
    }
}

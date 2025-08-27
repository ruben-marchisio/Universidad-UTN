package clase12;


import java.util.Scanner;


public class ejercicio2 {
    public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);

        // Pedir los valores al usuario
        System.out.print("Ingrese el valor de a: ");
        double a = scanner.nextDouble();

        System.out.print("Ingrese el valor de b: ");
        double b = scanner.nextDouble();

        // Calcular el cuadrado de a y b usando Math.pow
        double a2 = Math.pow(a, 2);
        double b2 = Math.pow(b, 2);
        double ab2 = 2 * a * b;

        // Sumar todos los componentes
        double resultado = a2 + b2 + ab2;

        // Mostrar el resultado
        System.out.println("El resultado de (a+b)^2 es: " + resultado);  
    }
}

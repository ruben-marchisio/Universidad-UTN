
import java.util.Scanner;


public class ejercicio7 {
    //una compania de ventas de carros usados, paga a su personal de ventas 
    //un salario de 1000 mensuales mas una comision de 150 por cada carro vendido
    //mas el 5% del valor de la venta por carro cada mes el capturista de la empresa 
    //ingresa en la computadora los datos pertinentes 
    //hacer un programa que calcule e imprima el salario mensual de un vendedor dado 
    // el salario de 1000 lo vamos a manejar como un dato constante para asignarlo debemos 
    // usar usar la palabra reservada final 
    
public static void main(String[] args) {
        // Declarar la constante para el salario base
        final double SALARIO_BASE = 1000.0;

        Scanner entrada = new Scanner(System.in);

        // Pedir al usuario la cantidad de autos vendidos
        System.out.print("Ingrese la cantidad de autos vendidos en el mes: ");
        int autosVendidos = entrada.nextInt();

        // Inicializar la suma total de los valores de los autos
        double sumaValores = 0;

        // Pedir al usuario el valor de cada auto vendido
        for (int i = 1; i <= autosVendidos; i++) {
            System.out.print("Ingrese el valor del auto #" + i + ": ");
            double valorAuto = entrada.nextDouble();
            sumaValores += valorAuto;
        }

        // Calcular comisión por cantidad de autos vendidos
        double comisionPorAutos = autosVendidos * 150;

        // Calcular comisión adicional del 5% del valor total de ventas
        double comisionPorVentas = sumaValores * 0.05;

        // Calcular el salario total
        double salarioTotal = SALARIO_BASE + comisionPorAutos + comisionPorVentas;

        // Mostrar el salario mensual del vendedor
        System.out.println("El salario mensual del vendedor es: $" + salarioTotal);

        entrada.close();
    }
}

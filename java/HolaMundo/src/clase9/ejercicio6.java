
import java.util.Scanner;


public class ejercicio6 {
    //gillermo tiene N dolares, luis tiene la mitad de que posee gillermo 
    //. juan tiene la mitad de lo que posee luis y gillermo justos.
    //hacer un programa que calcule e imprima la cantidad de dinero que tiene 
    //entrre los tres.
public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Pedir al usuario cuánto dinero tiene Guillermo
        System.out.print("Ingrese la cantidad de dólares que tiene Guillermo: ");
        double guillermo = entrada.nextDouble();

        // Luis tiene la mitad de lo que tiene Guillermo
        double luis = guillermo / 2;

        // Juan tiene la mitad de lo que poseen juntos Luis y Guillermo
        double juan = (guillermo + luis) / 2;

        // Calcular el total entre los tres
        double total = guillermo + luis + juan;

        // Mostrar el resultado
        System.out.println("La cantidad total de dinero entre los tres es: $" + total);

        entrada.close();
    }
}

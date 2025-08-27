
import java.util.Scanner;


public class ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Colocar un numero del mes: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "estacion desconocida";
        switch (mes) {
            case 1: case 2: case 3:
                estacion = "verano";
                break;
            case 4: case 5: case 6:
                estacion = "otonio";
                break;
            case 7: case 8: case 9:
                estacion = "invierno";
                break;
            case 10: case 11: case 12:
                estacion = "Primavera";
                break;
        }
        System.out.println("estacion = " + estacion);
    }
}

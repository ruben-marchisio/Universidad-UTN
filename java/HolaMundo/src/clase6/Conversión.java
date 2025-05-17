
import java.util.Scanner;


public class Conversión {
    public static void main(String[] args) {
        //conversion de tipos primitivos
        var edad = Integer.parseInt("20"); // lo convierte en tipo entero 
        System.out.println("edad =" + edad + 1);
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI" + valorPI);
       
        var entrada = new Scanner(System.in);
        System.out.println("Colocar la edad");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad =" + edad);
              
        
    }
}

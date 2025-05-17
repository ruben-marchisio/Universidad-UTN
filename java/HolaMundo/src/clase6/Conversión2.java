
import java.util.Scanner;


public class Conversión2 {
    public static void main(String[] args) {
    var edadTexto = String.valueOf(10);
    System.out.println("edadTexto" + edadTexto);
        
    var fraseChar = "programadores".charAt(4);
     System.out.println("fraseChar =" + fraseChar);
        
        System.out.println("Colocar un caracter");
        var entrada = new Scanner(System.in);
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar =" + fraseChar);
    }
  
}

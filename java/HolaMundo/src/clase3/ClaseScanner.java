
import java.util.Scanner;


public class ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingresar su nombre ");
        var usuario = entrada.nextLine();
        System.out.println("el nombre es " + usuario);
        System.out.println("Cual es su apellido");
        var usuario2 = entrada.nextLine();
        System.out.println("su nombre completo es " + usuario + " " +usuario2);
                                                                               
    }
}

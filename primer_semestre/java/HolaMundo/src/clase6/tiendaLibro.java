
import java.util.Scanner;


public class tiendaLibro {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingresar el nombre del libro");
        String nombreLibro = entrada.nextLine();
        System.out.println("Colocar el ID");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Colocar el precio del libro ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirmar si el envio es gratis");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro+""+idLibro);
        System.out.println("Precio del libro: "+ precioLibro);
        System.out.println("el evio es: "+envioGratuito);
        
        
        
    
    }
}

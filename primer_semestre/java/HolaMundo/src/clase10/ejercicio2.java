
package clase10;

import java.util.Scanner;


public class ejercicio2 {
    
    public static void main(String[] args) {
      Scanner entrada = new Scanner(System.in);
        System.out.println("Colocar un numero del 1 al 5: ");
      var numero = Integer.parseInt(entrada.nextLine());
      var numeroTexto = "valor desconocido";
      switch(numero){
          case 1:
              numeroTexto = "numero 1";
              break;
          case 2:
              numeroTexto = "numero 2";
              break;
          case 3:
              numeroTexto = "numero 3";
              break;
         case 4:
              numeroTexto = "numero 4";
              break;
         case 5:
              numeroTexto = "numero 5";
              break;
         default:
             numeroTexto = "numero no encontrado";
      }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}


public class SentenciaControlIFelse {
    public static void main(String[] args) {
        var condicion = true;
        if (condicion) {
            System.out.println("condicion = " + condicion);
    }
        else {
            System.out.println("condicion = " + condicion); 
        }
        var numero = 31;
        var numeroTexto = "numero desconocido";
        if (numero == 1) {
            numeroTexto = "numero 1";
         
        }
        else if (numero == 2) {
            numeroTexto = "numero 2";
        }
        else if (numero == 3) {
            numeroTexto = "numero 3";
        }
        else if (numero == 4) {
            numeroTexto = "numero 4";
        }
        else {
            numeroTexto = "numero no fue encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}

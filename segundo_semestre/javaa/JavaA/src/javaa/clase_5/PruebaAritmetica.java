// 5.1 Clase Aritmética: Creamos un objeto
package javaa.clase_5;


public class PruebaAritmetica {
    public static void main(String[] args) {
        // Crear objeto de tipo Aritmetica
        Aritmetica aritmetica1 = new Aritmetica();

        // Asignar valores
        aritmetica1.a = 3;
        aritmetica1.b = 3;

        // Llamar al método
        aritmetica1.sumarNumeros();
    }
}

// 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug
// 5.3 Paso de argumentos a un método
// 5.4 Un método llamando a otro método
// 5.5 Operador this

package javaa.clase_5;


public class AritmeticaCreamosMetodo {
    public static void main(String[] args) {
        Aritmetica aritmetica2 = new Aritmetica();
        
        aritmetica2.a = 3;
        aritmetica2.b = 5;
        
        int resultado = aritmetica2.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica2.sumarConArgumentos(10, 11);
        System.out.println("resultado usando argumentos =" + resultado);
    }
    

}


public class ConcatenaciónEjercicio {

    public static void main(String[] args) {
        var usuario = "carlos ";
        var titulo = "albañil";
        //unimos las fraces 
        var union = usuario + titulo;

        System.out.println(union);
        
        //suma 
        var numero = 21;
        var numero2 = 9;
        
        var suma = numero + numero2;
        
        System.out.println(suma);
        //otra manera 
        System.out.println(usuario + (numero + numero2));//devemos prorizar la suma 
    }
}

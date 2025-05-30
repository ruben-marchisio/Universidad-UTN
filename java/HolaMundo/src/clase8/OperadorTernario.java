
public class OperadorTernario {
    public static void main(String[] args) {
        // operador ternario
        var resultadoT = (5 > 8)? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "par" : "impar";
        System.out.println("numeroT = " + numeroT);
        //Se recomienda solo usar cuando son expresiones simples pero no cuando son mas complejas 
    }
}

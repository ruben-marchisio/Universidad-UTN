
public class OperadoresAsignación {
    public static void main(String[] args) {
        //operadores de asignacion
        int varNum1 = 1 , VarNum2 = 4;
        int varNum3 = varNum1 + 6 - VarNum2;
        System.out.println("varNum3 = " + varNum3);
        
        //operador o de composicion
        
        varNum1 += 1; // seria lo mismo que varNum1 = varNum1 + 1 pero mas corto 
        System.out.println("varNum1 suma = " + varNum1);
        varNum1 -= 3;
        System.out.println("varNum1 resta = " + varNum1);
        varNum1 *= 6;
        System.out.println("varNum1 multi = " + varNum1);
        varNum1 %= 2;
        System.out.println("varNum1 divi= " + varNum1);
        varNum1 /= 4;
        System.out.println("varNum1 divi= " + varNum1);
    }
}

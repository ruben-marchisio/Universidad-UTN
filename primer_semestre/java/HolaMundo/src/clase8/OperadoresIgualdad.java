
public class OperadoresIgualdad {
    public static void main(String[] args) {
        //oèradores de igualdad y Relacionales 
        var aNum = 5;
        var bNum = 2;
        var cNum = (aNum == bNum);//camparamos dos valores para saber si son iguales 
        System.out.println("cNum = " + cNum);
        
        var dNum = (aNum != bNum); //copara si son distintas 
        System.out.println("dNum = " + dNum);
        
        //comapramos cadenas 
        var cadenaA = "hola";
        var cadenaB = "hola";
        var cVar = cadenaA == cadenaB;// solo hace una comparacion de referencia no de texto 
        System.out.println("cVar = " + cVar);
        
        //meto correcto de texto 
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
    }
}

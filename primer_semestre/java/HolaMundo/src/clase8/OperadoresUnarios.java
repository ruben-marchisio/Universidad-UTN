
public class OperadoresUnarios {
    public static void main(String[] args) {
        //operadores UNARIOS: cambio de signo 
        var varA = 7;
        var varB = -varA; //eñ numero 7 pasara hacer negativo 
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
        
        //Operador de Negacion
        var varC = true; // este es de tipo boolean verdadero 
        var varD = !varC;// ahora pasara a ser falso 
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores Unarios de incremento: Preincremento 
        var varE = 9;//se incrementa el valor
        var varF = ++varE; 
        //primero se incrementa la variable y depsues se una su valor
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
      
        //Postincremento
        var varG = 3;
        var varH = varG++;//primero el valor de la variable, luego el incremento 
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //operadores Unarios de decremento: Predecremento 
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        
        //Postdecremento 
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
        
              
    }
}


public class OperadoresAritméticos {
    public static void main(String[] args) {
        //la forma de inicializar varias variables no se puede con var
        int num1 = 5 , num2 = 4;
        //sumamos los resultados
        var solucion = num1 + num2;
        System.out.println("solucion de la suma =" + solucion);
        
        //restamos los resultados 
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        //los multiplicamos 
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        //hacemos una division 
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        //un metodo que podemos hacer para que el resultado de la division sea un decimal o float
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 = " + solucion2);
        
        // para tener el residuo entero de una division
        solucion = num1 % num2;
        System.out.println("solucion = " + solucion);
        
        //comparamos si un numero es par o impar
        if (num1 % 2 == 0)
            System.out.println("es un numero par");
        else
            System.out.println("Es un nemero impar");
      
    }
 
}

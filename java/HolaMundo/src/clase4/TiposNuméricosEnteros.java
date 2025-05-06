package clase4;

public class TiposNuméricosEnteros {
    public static void main(String[] args) {
        //si sumeramos en rango permitido no mostrar el valor o tira error 
        byte numEnteroByte = 10;
        System.out.println("valor minimo del byte " + Byte.MIN_VALUE);
        System.out.println("valor maximo del byte " + Byte.MAX_VALUE);
        
        //el tipo short
        short numeroShort = 4234;
        System.out.println("valor de Short "+ numeroShort);
        System.out.println("valor minimo del Short " + Short.MIN_VALUE);
        System.out.println("valor maximo del Short " + Short.MAX_VALUE);
        
        //el tipo int 
        
        int numEnteroInt = 13564;
        System.out.println("valor de Short "+ numEnteroInt);
        System.out.println("valor minimo del int " + Integer.MIN_VALUE);
        System.out.println("valor maximo del int " + Integer.MAX_VALUE);
        
        //el tipo long
        
        long numEnterolong = 13546;
        System.out.println("valor de Short "+ numEnterolong);
        System.out.println("valor minimo del  long " + Long.MIN_VALUE);
        System.out.println("valor maximo del  long " + Long.MAX_VALUE);
    }
}

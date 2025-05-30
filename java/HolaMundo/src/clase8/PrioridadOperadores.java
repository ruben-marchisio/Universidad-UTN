
public class PrioridadOperadores {
    public static void main(String[] args) {
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        
        var solucionArimetica = 4 + 5 * 6 / 3; 
        System.out.println("solucionArimetica = " + solucionArimetica);
        
        solucionArimetica = (4+5) * 6 / 3;
        System.out.println("solucionArimetica = " + solucionArimetica);
                
        
    }
   
}

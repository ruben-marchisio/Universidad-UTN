
public class OperadoresCondicionales {

    public static void main(String[] args) {
        // operador lógico AND 

        var valorA = 7;
        var valorMinim = 0;
        var valorMaxi = 10;
        var respuesta = valorA >= 0 && valorA <= 10; // los dos tiene que ser v si uno no lo es es F

        if (respuesta) {
            System.out.println("Esta dentro del rago");
        } else {
            System.out.println("Esta fuera del rango");
        }

        //operador OR
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) //conque uno sea V resultado V
        {
            System.out.println("Puede ir al juego");
        } else {
            System.out.println("no puede ir ");
        }

    }
}

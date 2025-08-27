package ejercicios;

/*
Lo que deben enviar es el ejercicio, Detalles Libro

1. Pregunta o pide el nombre del libro

2. Pregunta o pide el autor del libro

3. Muestra por consola la información: nombreLibro+ " fue escrito por "+ nombreAutor

4. Van a tener que utilizar la clase Scanner


 */
import java.util.Scanner; // Importa la clase Scanner para la entrada de datos desde el teclado

public class ejercicio { // Declara la clase pública llamada Jasasd
    public static void main(String[] args) { // Método principal: punto de entrada del programa
        // Crea un objeto Scanner para capturar la entrada del usuario
        Scanner entrada = new Scanner(System.in);

        // Muestra un mensaje pidiendo el nombre del libro
        System.out.println("Por favor ingresar el nombre del libro ");
        // Captura la entrada del usuario y la guarda en la variable nombreLibro
        String nombreLibro = entrada.nextLine();

        // Muestra un mensaje pidiendo el nombre del autor
        System.out.println("Ahora ingresar el nombre del autor");
        // Captura la entrada del usuario y la guarda en la variable nombreAutor
        String nombreAutor = entrada.nextLine();

        // Muestra el resultado combinando el nombre del libro y el autor
        System.out.println("El libro elegido fue: " + nombreLibro + " escrito por: " + nombreAutor);
    }
}

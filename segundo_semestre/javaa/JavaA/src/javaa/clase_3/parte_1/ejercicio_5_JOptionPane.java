package javaa.clase_3.parte_1;

import javax.swing.JOptionPane;

public class ejercicio_5_JOptionPane {
     public static void main(String[] args) {
        // Generar número aleatorio entre 0 y 100
        int numeroSecreto = (int) (Math.random() * 101);
        int intento;
        int contador = 0;

        JOptionPane.showMessageDialog(null, "Juego: Adivina el número (entre 0 y 100)");

        do {
            // Pedimos número al usuario
            String input = JOptionPane.showInputDialog("Introduce un número:");
            intento = Integer.parseInt(input);
            contador++;

            if (intento < numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número secreto es MAYOR");
            } else if (intento > numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número secreto es MENOR");
            } else {
                JOptionPane.showMessageDialog(null,
                        "¡Acertaste! El número era " + numeroSecreto +
                        "\nLo lograste en " + contador + " intentos.");
            }

        } while (intento != numeroSecreto);
    }
}

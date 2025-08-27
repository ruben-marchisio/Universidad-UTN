package javaa.clase_3.parte_1;

import javax.swing.JOptionPane;

public class ejercicio_JOptionPane_3 {
     public static void main(String[] args) {
        int numero;
        
        do {
            // Mostramos un cuadro de diálogo para pedir el número
            String input = JOptionPane.showInputDialog("Ingrese un número (0 para salir):");
            
            // Convertimos el texto a número entero
            numero = Integer.parseInt(input);
            
            // Si no es cero, evaluamos si es par o impar
            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, numero + " es par.");
                } else {
                    JOptionPane.showMessageDialog(null, numero + " es impar.");
                }
            }
            
        } while (numero != 0); // Repite hasta que se ingrese 0
        
        JOptionPane.showMessageDialog(null, "Programa finalizado.");
    }
}



package javaa.clase_5;


public class Aritmetica {
    // Atributos
    int a;
    int b;

    // Método
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }
    
    public int sumarConRetorno(){

        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; // el argumento a se asigna al atributo this.a (es obcional)
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno();
    }
}

import java.util.Scanner;

public class AreaCirculo {
    public static void main(String[] args) {

        double pi = 3.14;
        double r;
        double a;

        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite o valor do raio: ");
        r = teclado.nextDouble();

        a = pi * r * r;

        System.out.println("A área do círculo é: " + a);

        teclado.close();
    }
}

package calculadora;

import java.util.Scanner;

public class Index {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scan = new Scanner(System.in);
		int a,b;
		
		System.out.println("Informar o primeiro numero: ");
		a= scan.nextInt();
		System.out.println("Informar o segundo numero: ");
		b=scan.nextInt();
		
	
		int soma = soma(a,b);
		int subtracao =subtracao(a,b);
		int mult = mult(a,b);
		double divisao = divisao(a,b);
		
		
		System.out.println(soma);
		System.out.println(subtracao);
		System.out.println(mult);
		System.out.println(divisao);
		
		
		
	
		
	}
	

	public static int soma(int a, int b) {

		return a + b;
	}

	public static int subtracao(int a, int b) {

		return a - b;
	}

	public static int mult(int a, int b) {

		return a * b;
	}

	public static double divisao(double a, double b) {
		return a / b;
	}
}

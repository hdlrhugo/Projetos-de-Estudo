package metodos;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("EXERCICIO DE CALCULADORA ");
		
		
		//calculadora
		Calculadora.soma(3, 6);
		Calculadora.subtracao(9,1.8);
		Calculadora.multiplicacao(7,8);
		Calculadora.divisao(5,2.5);
		
		//Mensagem
		System.out.println();
		System.out.println("EXERCICIO DE MENSAGEM");
		Mensagem.obterMensagem(9);
		Mensagem.obterMensagem(14);
		Mensagem.obterMensagem(1);
		
		//Emprestimo
		System.out.println();
		System.out.println("EXERCICIO DE EMPRESTIMO");
		
		Emprestimo.calcular(1000,Emprestimo.getDuasParcelas());
		Emprestimo.calcular(1000,Emprestimo.getTresParcelas());
		Emprestimo.calcular(1000,5);

	}

}
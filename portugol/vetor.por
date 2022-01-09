programa
{
	
	funcao inicio()
	{
		inteiro vetor[]={22,4,7,8,87}
		inteiro numero
		logico achou=falso


		escreva("Qual numero deseja procurar? ")
		leia(numero)

		 para(inteiro i=0;i<5;i++){
		 	se(vetor[i]==numero){
		 		escreva("você achou, ABESTADO!!"+i+ "\n")
		 		achou=verdadeiro
		 		}
		 		
		 	}
		se(nao achou){
			escreva("O numero não esta dentro do vetor. \n")
			}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 381; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
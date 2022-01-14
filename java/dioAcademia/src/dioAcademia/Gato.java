package dioAcademia;

import java.util.Objects;

public class Gato {
	
	private String name;
	private String cor;
	private int idade;
	public Gato() {
		
		
	}
	public Gato(String name, String cor, int idade) {
		
		this.name = name;
		this.cor = cor;
		this.idade = idade;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getCor() {
		return cor;
	}
	public void setCor(String cor) {
		this.cor = cor;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	@Override
	public int hashCode() {
		return Objects.hash(cor, idade, name);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Gato other = (Gato) obj;
		return Objects.equals(cor, other.cor) && idade == other.idade && Objects.equals(name, other.name);
	}
	@Override
	public String toString() {
		return "Gato [name=" + name + ", cor=" + cor + ", idade=" + idade + "]";
	}
	
	/*public Gato(String nome,String cor, int idade) {
		
		this.name=nome;
		this.cor=cor;
		this.idade=idade;
	}*/
}

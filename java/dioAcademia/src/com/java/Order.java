package com.java;

public class Order {
	
	private final String code;
	private final int totalValor;
	
	private String[] items;
	
	public Order(String code , int totalValor) {
		this.code=code;
		this.totalValor=totalValor;
		
		
	}
	
	public void printItens() {
		
		int i=0;
		 while (i< items.length) 
		 {
			 System.out.println(items[i]);
			 i++;
		 }
		 
	}

}

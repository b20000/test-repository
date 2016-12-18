package com.test;

public class FizzBuzzThread extends Thread {

	/**
	 * @param args
	 */
	private static Object lock = new Object();
	protected static int current = 1;
	private int max ;
	private boolean div3,div5; 
	
	private String toPrint;
	
	
	public FizzBuzzThread(boolean div3, boolean div5, int max, String toPrint){
		
		this.div3 = div3;
		this.div5 = div5;
		this.max = max;
		this.toPrint = toPrint;
	}
	
	public void print(){
		
		System.out.println(toPrint);
	}
	
	public void run() {
		
		while (true){
			
			synchronized(lock){
				
				if ( current > max ){
					return;
				}
				
				if ((current %3 == 0) == div3 && (current %5 == 0) == div5){
					print();
					current ++;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n=100;
		Thread[] threads = { new FizzBuzzThread(true,true,n,"FizzBuzz"),
				 new FizzBuzzThread(true,true,n,"Fizz"),
				 new FizzBuzzThread(true,true,n,"Buzz"),
				 new NumberThread(false,false, n),
				};
		
		for ( Thread thread : threads){
			
			thread.start();

	}

}
	
}

class NumberThread extends FizzBuzzThread{
	
	public NumberThread(boolean div3, boolean div5, int max){
		
		super(div3, div5, max, null);
	}
	
	public void print(){
		System.out.println(current);
	}
}

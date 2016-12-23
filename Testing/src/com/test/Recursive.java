package com.test;

public class Recursive {

	public static long fibonacci(int num){
		
		if ( num == 0)
			return 0;
		else if ( num == 1)
			return  1;
		else
			return fibonacci(num -1) + fibonacci(num -2);
	}
	
	public static long factorial( int num){
		if (num < 1)
			return num;
		else 
			return  num * factorial ( num -1 );
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/* int n = 5;
		for (int i = 1; i <= n; i++)
            System.out.println(i + ": " + fibonacci(i));*/
		
		System.out.println(factorial(5));
	}

}

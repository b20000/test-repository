package com.test;

public class Fibonacci {

public static long fibonacci(int num){
		
		if ( num == 0)
			return 0;
		else if ( num == 1)
			return  1;
		else
			return fibonacci(num -1) + fibonacci(num -2);
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 int n = 5;
		for (int i = 1; i <= n; i++)
            System.out.println(i + ": " + fibonacci(i));
	}

}

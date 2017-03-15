package com.test;

import java.io.BufferedReader;
import java.io.FileReader;

public class ScrapeCode {

	/**
	 * @param args
	 */
	
	 public static void multTables ( int max )
	    {
	        for ( int i = 1; i <= max; i++ ) {
	            for ( int j = 1; j <= max; j++ ) {
	                System.out.print ( String.format ( "%4d", j * i ));
	            }
	            System.out.println();
	        }
	    }
	 public static void sumFile ( String name ) {
	        try {
	            int total = 0;
	            BufferedReader in = new BufferedReader ( new FileReader ( name ));
	            for ( String s = in.readLine(); s != null; s = in.readLine() ) {
	                total += Integer.parseInt ( s );
	            }
	            System.out.println ( total );
	            in.close();
	        }
	        catch ( Exception xc ) {
	            xc.printStackTrace();
	        }
	    } 
	 
	 public static void printOdds() {
	        for (int i = 1; i < 100; i += 2) {
	            System.out.println ( i );
	        }
	    }
	 
	 public static int largest ( int[] input ) {
		    int max = Integer.MIN_VALUE;
		    for ( int i = 0; i < input.length; i++ ) {
		        if ( input[i] > max ) max = input[i];
		    }
		    return max;
	 } 
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ScrapeCode objSC = new ScrapeCode();
		//objSC.multTables(5);
		objSC.printOdds();
	}

}

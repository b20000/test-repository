package com.test;

import java.util.Arrays;

public class Test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String comm = "Job failed, attempt 2/2, Occured at:01/21/2014, group=re-try";
		Boolean status = false;
		
		if ( Arrays.asList(comm.split(",")).contains("Job failed") || ( status != null && status == false )) {
			 System.out.println("I am here");
		}
	}

}

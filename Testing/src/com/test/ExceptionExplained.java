package com.test;
import java.io.*;  



class ParentException{
	
	//Below is the compile time error.
	
/*
  void msg(){System.out.println("parent");}  
}  
  
class TestExceptionChild extends ParentException{  
  void msg()throws IOException{  
    System.out.println("TestExceptionChild");  
  }  
 */

	
	void msg(){System.out.println("parent");} 
	
	
	
}

	class TestExceptionChild1 extends ParentException{  
		  
		void msg()throws ArithmeticException{  
		    System.out.println("child");  
		  }  
	 
}
public class ExceptionExplained {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ParentException p= new TestExceptionChild1();  
		p.msg();
	}

}

package com.test;

public class OverloadingConcepts {

	 //Simple overloading.
	 void sum(int a,int b){
		 System.out.println(a+b);
	 }  
	 void sum(int a,int b,int c){
		 System.out.println(a+b+c);
	 }  
	 
	 
	 //Overloading by different data type.
	 
	 void sum1(int a,int b){
		 System.out.println(a+b);
	 }  
	 void sum1(double a,double b){
		 System.out.println(a+b);
	 } 
	  
	 //Not supported in Java-Compile time error.
	 
	 //int sum3(int a,int b){System.out.println(a+b);}  
	 //double sum3(int a,int b){System.out.println(a+b);} 
	  
	 //Type promotion concept.
	 
	 void sum4(int a,long b){
		 System.out.println(a+b);
	 }  
	 void sum4(int a,int b,int c){
		 System.out.println(a+b+c);
	
	 } 
	 
	 //Type promotion if matching is found
	 void sum5(int a,int b){
		 System.out.println("int arg method invoked");
	 }  
	 void sum5(long a,long b){
		 System.out.println("long arg method invoked");
	 }  
	  
	 //Type promotion ambiguity but no error while definition.
	 
	 void sum6(int a,long b){
		 System.out.println("a method invoked");
	 }  
	 void sum6(long a,int b){
		 System.out.println("b method invoked");
	 }  
	
	 
	 
	 public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		OverloadingConcepts objOver = new OverloadingConcepts();
		//By different argument.
		objOver.sum(10, 20);
		objOver.sum(10,20,30);
		
		//By different data type.
		objOver.sum1(10, 20);
		objOver.sum1(10, 20);
		
		//Type promotion
		objOver.sum4(10, 20);//int in 2nd argument is automatically promoted to long.
		objOver.sum4(10,20,30);
		
		//Type promotion with matching
		//By different data type.
		objOver.sum5(10, 20);//now int arg sum() method gets invoked 
		
		//Type promotion compile time error. Throws ambiguity error
		
		//objOver.sum6(10, 20);
		
	}

}

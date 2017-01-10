package com.test;
//Example of method overriding in sub class.

class Bank{  
	int getRateOfInterest(){return 0;}  
}  
  
class Citi extends Bank{  
	int getRateOfInterest(){return 8;}  
}  
  
class Chase extends Bank{  
	int getRateOfInterest(){return 7;}  
}  
class Boa extends Bank{  
	int getRateOfInterest(){return 9;}  
}  
  
public class MethodOverridingDemo{  

		public static void main(String args[]){  
			Citi c = new Citi();  
			Chase ch = new Chase();  
			Boa b = new Boa();  
			
			System.out.println("Citi Rate of Interest: "+c.getRateOfInterest());  
			System.out.println("Chase Rate of Interest: "+ch.getRateOfInterest());  
			System.out.println("BOA Rate of Interest: "+b.getRateOfInterest());  
		}  
}  

package com.java.factory;

//Seperate class and file. 
interface Currency {
    String getSymbol();
}


//Concrete Rupee Class code . Ideally the concreate class should be in seperate files. 
class Rupee implements Currency {
    @Override
    public String getSymbol() {
           return "Rs";
    }
}

//Concrete SGD class Code
class SGDDollar implements Currency {
    @Override
    public String getSymbol() {
           return "SGD";
    }
}

//Concrete US Dollar code
class USDollar implements Currency {
    @Override
    public String getSymbol() {
           return "USD";
    }
}

class CurrencyFactory {

    public static Currency createCurrency (String country) {
    if (country. equalsIgnoreCase ("India")){
           return new Rupee();
    }else if(country. equalsIgnoreCase ("Singapore")){
           return new SGDDollar();
    }else if(country. equalsIgnoreCase ("US")){
           return new USDollar();
     }
    throw new IllegalArgumentException("No such currency");
    }
}


// Factory client code



public class Factory {
      public static void main(String args[]) {
             //String country = args[0];
             
             //Passing it here for testing
             String country="India";
             Currency objFactory = CurrencyFactory.createCurrency(country);
             System.out.println("Currency for country " + country + " is : " + objFactory.getSymbol());
      }
}
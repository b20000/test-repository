package com.java.singleton;


	public class LazyInitializationSingleton
	{
	    
	    private static  volatile LazyInitializationSingleton  uniqueInstance;
	    
	    private LazyInitializationSingleton(){}
	    
	    public static   LazyInitializationSingleton  getInstance()
	    {
	        if (uniqueInstance ==null )
	        {
	            synchronized(LazyInitializationSingleton.class)
	            {
	                if (uniqueInstance ==null )
	                {
	                    uniqueInstance=new LazyInitializationSingleton();
	                }
	            }
	        }
	        return uniqueInstance ;
	    }
	    
	    // other useful methods here
	}

package com.java.singleton;

public class EarlyInitializationSingleton
{
    
    private static EarlyInitializationSingleton  uniqueInstance  =  new EarlyInitializationSingleton();
    
    private EarlyInitializationSingleton(){}
    
    public static  EarlyInitializationSingleton  getInstance()
    {
        return  uniqueInstance ;
    }
    
    // other useful methods here
}
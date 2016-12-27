package com.java.singleton;

public class JavaSingleton
{
    
    private static JavaSingleton  uniqueInstance;
    
    private JavaSingleton(){}
    
    public static  synchronized  JavaSingleton  getInstance()
    {
        if (uniqueInstance ==null )
        {
            uniqueInstance=new JavaSingleton();
        }
        return uniqueInstance ;
    }
    
    // other useful methods here
}
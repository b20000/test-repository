package com.java.decorator;
import java.math.BigDecimal;

/**
 * Base class for Decorators, this class inherit from Sandwich, so that
 * it can be of same type, which is required to pass decorators where
 * original object is expected. Later, this class will also come handy
 * to provide common functionalities to Decorators.
 *
 * @author
 */
public abstract class SandWichDecorator extends Sandwich {  
   
    @Override
    public abstract BigDecimal price();
   
}

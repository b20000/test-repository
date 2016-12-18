package com.java.decorator;

import java.math.BigDecimal;

/**
 * A Decorator class, which adds cheese (new functionality) into Sandwich object.
 * This Decorator class modifies price() and getDescritption() method to implement
 * new behaviour.
 *
 * @author
 */
public class ChickenDecorator extends SandWichDecorator{
    Sandwich currentSandwich;
   
    public ChickenDecorator(Sandwich sw){
        currentSandwich = sw;
    }
   
    @Override
    public String getDescription(){
        return currentSandwich.getDescription() + ", Chicken";
    }
    @Override
    public BigDecimal price() {
        return currentSandwich.price().add(new BigDecimal("1.50"));
    }
   
}
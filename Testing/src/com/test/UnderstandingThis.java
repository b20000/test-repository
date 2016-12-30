package com.test;

class Parent {

    int i;
    Parent() {
        this.i = 5;
    }

    void doStuff() {
        System.out.println(this.i);
    }
}

class Child extends Parent {
    int i;
    Child() {
        this.i = 7;
    }
}

public class UnderstandingThis {

    public static void main(String[] args) {
        Child m = new Child();
        System.out.println(m.i); //print 7
        m.doStuff(); //print 5
    }
}

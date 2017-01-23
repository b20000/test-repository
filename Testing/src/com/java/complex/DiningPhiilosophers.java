package com.java.complex;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// This is a simple implementation without any fix to deadlock.
class Chopstick {
	private Lock lock;
	
	public Chopstick(){
		lock = new ReentrantLock();
	}
	
	public void pickup(){
		lock.lock();
	}
	
	public void putdown(){
		lock.unlock();
	}
}

class Philosopher extends Thread{
	
	private int bites = 10;
	private Chopstick left, right;
	
	public Philosopher(Chopstick left,Chopstick right){
		this.left = left;
		this.right = right;
	}
	
	public void eat(){
		pickup();
		chew();
		putdown();
	}
	
	public void pickup(){
		left.pickup();
		right.pickup();
	}
	
	public void chew(){}
	
	public void putdown(){
		left.putdown();
		right.putdown();
	}
	
	public void run(){
		for ( int i=0;i<bites;i++){
			eat();
		}
	}
}


public class DiningPhiilosophers {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Philosopher objP = new Philosopher(left,right);
	}

}

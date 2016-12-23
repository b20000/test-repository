package com.test;

import java.util.Vector;

import javax.swing.JFrame;

public class BackgroundMethod extends Thread {

    public static void main(final String[] args) {

       //MyBackgroudMethod thread = new MyBackgroudMethod();
       // thread.setDaemon(true);
       // thread.start();

    	
       /* java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                JFrame jFrame = new JFrame();
                jFrame.setSize(200, 200);
                jFrame.setVisible(true);
            }
        });*/
        //@Override
        new Thread(){
        public void run() {
        	Vector v = new Vector();
        	boolean exit_loop = true;
            while (exit_loop) {
                //System.out.println("Executed!");
            	 byte b[] = new byte[1048576];
                 v.add(b);
                 Runtime rt = Runtime.getRuntime();
                 
                 if ( rt.freeMemory() <= 4048576789l ){
                	 exit_loop = false;
                	 System.out.println( "Exiting loop as system memory is reduced to certain number: " + rt.freeMemory() );
                 }
                 System.out.println( "free memory: " + rt.freeMemory() );
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
        }.start();
        
    }

   /*public static class MyBackgroudMethod extends Thread {

        @Override
        public void run() {
            while (true) {
                System.out.println("Executed!");
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

    }*/

}

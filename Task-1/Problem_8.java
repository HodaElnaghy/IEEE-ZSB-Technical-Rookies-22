/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_8;

import java.util.Scanner;
import java.util.Random;
public class Problem_8 {

   public static void main(String args[]) {
        int x = (int)(Math.random()*(11-1)+1);
        int counter =1;
        Scanner sc= new Scanner(System.in);
        int num = sc.nextInt();        
        
        while(num != x){
            System.out.println("wrong guess");
            counter ++ ;
             num = sc.nextInt();
            }
        System.out.println("Yay you got it "+counter+" tries");

        
    }
}
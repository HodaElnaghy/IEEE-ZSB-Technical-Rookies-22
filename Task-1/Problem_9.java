/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_9;

import java.util.Scanner;
import java.math.BigInteger;


public class Problem_9 {
    
    public static void main(String[] args) {
        System.out.println("Enter a number to find generates the first n fibonacci numbers. ");
        Scanner sc=new Scanner(System.in);  
        int num =sc.nextInt();   
       Fibo(num);
    }
    static void Fibo(int n){
        BigInteger num1= new BigInteger("0");
        BigInteger num2= new BigInteger("0");
        BigInteger num3= new BigInteger("1");
        if(n>0)
        {
            
            for(int i = 1; i <= n; i++)
            {
                num1 = num2;
                num2 = num3;
                num3 = num1.add(num2);
                System.out.print(num1+" ");
            }
        }
    
    }
}
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_6;

import java.util.Scanner;

public class Problem_6 {

  
    public static void main(String[] args) {
       System.out.println("Enter a number the sum of the numbers from 1 to n");
        int n, sum=0;  
        Scanner sc=new Scanner(System.in);  
        n=sc.nextInt();   
        if(n>0){
            for(int i=1 ;i<=n;i++)
            sum +=i;
        System.out.println("Sum = " + sum);
            
        }
    }
    
}

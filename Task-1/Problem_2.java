/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_2;

import java.util.Scanner;
public class Problem_2 {

      public static void main(String args[])
    {
        System.out.println("Enter the number to print all prime numbers smaller than or equal it");
        Scanner sc=new Scanner(System.in);  
        int n =sc.nextInt();  
       
        System.out.print("Following are the prime numbers ");
        System.out.println("smaller than or equal to " + n);
        Prime(n);
    } 
      
    public static void Prime(int n)
    {
       
        boolean prime[] = new boolean[n+1];
        for(int i=0;i<=n;i++)
            prime[i] = true;
         
        for(int p = 2; p*p <=n; p++)
        {
           
            if(prime[p] == true)
            {
                
                for(int i = p*p; i <= n; i += p)
                    prime[i] = false;
            }
        }
         
        
        for(int i = 2; i <= n; i++)
        {
            if(prime[i] == true)
                System.out.print(i + " ");
        }
    }
     
    
  
    
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_1;

import java.util.Scanner;

import java.util.Scanner;
public class Problem_1 {

     public static void main(String[] args) {
    System.out.println("Enter the length and the width of rectangle");
        Scanner sc=new Scanner(System.in);  
        int L =sc.nextInt();   
        int W =sc.nextInt(); 
        System.out.println("The area  equals "+ (L*W) );
        System.out.println("The parameter equals " + (2*(L+W)));
    }
    
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_4;

/import java.util.Scanner;
public class Problem_4 {

    
    public static void main(String[] args) {
        int max=0,num;
        Scanner sc= new Scanner(System.in);
        String str= sc.nextLine();
        String[] words = str.split(" ");
        
        for (int i=0 ; i<words.length ; i++)
        { 
         //   System.out.println("* "+words[i]);
         num= words[i].length();
         if (num>max)
             max=num;      
        }
 
      System.out.println( Repeat("*",(max+4)));
       for (int i=0 ; i<words.length ; i++) {
           int x = max -words[i].length();
           System.out.println("* " + words[i]+ Repeat(" ", x) + " *");
       }
      System.out.println( Repeat("*",(max+4)));
        
    }
    public static String Repeat(String s, int n){
    String repeated = "";
    for(int i=0; i<n ; i++ )
    {
        repeated += s;
    }
    return repeated;
    }
}
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_5;

import java.util.Scanner;
import java.util.Random;

public class Problem_5 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int size= sc.nextInt();
        int [] arr = new int[size];
        for (int i=0;i<size;i++){
            arr[i]=sc.nextInt();
        }
        
        
        
       
        Function1(arr);
        Function2(arr);
        System.out.println(Function3(arr,arr.length));
        
    }

    public static void Function1 (int [] arr1){
    int sum1=0;
        for (int i =0; i<arr1.length; i++){
            sum1+=arr1[i];
        }
    System.out.println(sum1);
    }
    

    public static void Function2 (int [] arr1){
        int sum1=0;
        int count =0 ;
        while (count< arr1.length){
            sum1+=arr1[count];
            count++;
        }
    System.out.println(sum1);
    }
    
    public static int Function3 (int [] arr1 , int size){
        if (size==0) return 0; 
        
        int sum1=(arr1[size-1]+Function3(arr1,size-1));
        
        
        
        return sum1;
    }
    
    
}
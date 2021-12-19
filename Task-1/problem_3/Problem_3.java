/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problem_3;

import java.util.Scanner;

/**
 *
 * @author ahmed
 */
public class Problem_3 {

    /**
     * @param args the command line arguments
     */

    
    public static void main(String[] args) {
        int A []= {1,2,5,10,15,24,60,75,100};
        Scanner sc =new Scanner(System.in);  
        int key =sc.nextInt();  
        if (BinarySearch(A,0,A.length,key)==-1)
            System.out.println("not found");
        else System.out.printf("The number %d is found and its index is ",key,BinarySearch(A,0,A.length,key));  
        
    }
    
    public static int BinarySearch (int [] arr , int L , int H , int key ){
        if(L<=H){
           int mid = (L+H)/2;
           if (key==arr[mid]) 
               return mid;
           if (key>arr[mid])
               return BinarySearch (arr,mid+1,H,key);
           return BinarySearch(arr,L,mid-1,key);
           
        }
        else 
            return -1;
    }
}

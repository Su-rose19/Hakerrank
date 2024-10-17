//Java Stdin and Stdout I
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        scan.close();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        
    }
}
//Java If-Else
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if (N%2==1) {
            System.out.println("Weird");
        }
        else{
            if(N>=2 && N<=5){
                System.out.println("Not Weird");
            }
            else if(N>=6 && N<=20){
                System.out.println("Weird");
            }
            else{
                System.out.println("Not Weird");
            }
        }

        scanner.close();
    }
}

//Java Stdin and Stdout II
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine(); // To move the cursor to read a string, 
                         // initialize a scan.nextLine()
        String s = scan.nextLine();
        scan.close();
        // Write your code here.

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

//===============================================================
//Java Output Formatting

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                System.out.print(s1);
                for(int j = s1.length()+1; j<=15;j++){
                    System.out.print(" ");
                }
                int numDigits = String.valueOf(x).length();
                if(numDigits==3){
                    System.out.println(x);
                }
                else if(numDigits==2){
                    System.out.println("0"+x);
                }
                else{
                    System.out.println("00"+x);
                }
            }
            System.out.println("================================");

    }
}

//===============================================================
//Java loops I


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        for(int i=1;i<=10;i++)
        {
            System.out.println(N+" x "+i+" = "+N*i);
        }
        bufferedReader.close();
    }
}














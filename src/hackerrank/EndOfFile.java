package hackerrank;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class EndOfFile {

    public static void main(String[] args) {
        
    	Scanner sc = new Scanner(System.in);
    	
    	String entrada = sc.nextLine();
    	
    	int num = 1;
    	
    	do{ 
    		
    		System.out.println(num + " " + entrada);
    		num += 1;
    		
    		
    		entrada = sc.nextLine();
    		
    	}while(sc.hasNext());
    	
    	System.out.println(num + " " + entrada);
    	
    	sc.close();
    }
}
import java.util.stream.*;
import java.util.*;

class Solution {
    int sum = 0;
    public int[] solution(String s) {
        int count = 0;
        
        while(true){
            s = change(s);
            count++;
            System.out.println(s);
            
            if(s.equals("1")){
                break;
            }
        }
        
        return new int[]{count, sum};
    }
    
    public String change(String input){
        
        String next = input.replace("0", "");
        
        sum += (input.length() - next.length());
        
        return Integer.toBinaryString(next.length());
    }
}
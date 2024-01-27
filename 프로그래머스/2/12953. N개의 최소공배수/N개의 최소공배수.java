import java.util.stream.*;
import java.util.*;

class Solution {
    
    int[] ints;
    
    public int solution(int[] arr) {
        ints = new int[101];
        
        for(int i = 0; i < arr.length ; i++){
            toSoDiv(arr[i]);
        }
        
        int mul = 1;
        
        for(int i = 2; i < ints.length;i++){
            for(int j = 0;j < ints[i]; j++){
                mul *= i;
                System.out.println(mul);
            }
        }
        
        return mul;
    }
    
    public void toSoDiv(int n){
        
        int temp = 0;
        
        int i = 2;
        
        while(n > 1){
            if(n % i == 0){
                temp++;
                if(ints[i] < temp){
                    ints[i] = temp;
                }
                
                n = n / i;
                continue;
            }
            temp = 0;
            i++;
        }
    }
}
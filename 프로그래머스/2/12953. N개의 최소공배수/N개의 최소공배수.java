import java.util.stream.*;
import java.util.*;

class Solution {
    public int lcm(int a, int b){
        int sourceMin = Math.min(a, b);
        int sourceMax = Math.max(a, b);
        int min = sourceMin;
        int max = sourceMax;
        
        while(max != min){
            if (min < max) min += sourceMin;
            else max += sourceMax;
        }
        
        return max;
    }
    
    public int solution(int[] arr) {
        int temp = 1;
        for(int i : arr){
            temp = lcm(temp, i);
        }
        return temp;
    }
}
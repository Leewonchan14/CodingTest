import java.util.stream.*;
import java.util.*;
class Solution {
    int[] arr;
    public int solution(int[] elements) {
        arr = elements;
        // arr = new int[]{1,2,3,4};
        Set<Integer> set = new HashSet<>();
        for(int i = 1; i <= arr.length; i++){
            for(int j = 0; j < arr.length; j++){
                set.add(getInt(j, i));
            }
        }
        
        return set.size();
    }
    
    public int getInt(int n, int len){
        int sum = 0;
        for(int i = n; i - n < len ; i++ ){
            if(arr.length > i){
                sum += arr[i];
                continue;
            }
            
            sum += arr[i - arr.length];
        }
        return sum;
    }
}
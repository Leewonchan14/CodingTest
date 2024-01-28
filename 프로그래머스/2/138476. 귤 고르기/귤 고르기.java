import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int[] arr = new int[10000001];
        for(int i : tangerine){
            arr[i]++;
        }
        
        Arrays.sort(arr);
        
        int lastIndex = arr.length - 1;
        
        int count = 0;
        while(k > 0){
            count++;
            k -= arr[lastIndex];
            lastIndex--;
        }
        
        return count;
        
        
    }
}
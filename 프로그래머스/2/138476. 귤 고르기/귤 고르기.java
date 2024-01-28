import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i : tangerine){
            if(!map.containsKey(i)){
                map.put(i,1);
                continue;
            }
            map.put(i,map.get(i) + 1);
        }
        
        int[] arr =map.values().stream().sorted().mapToInt(Integer::intValue).toArray();
        
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
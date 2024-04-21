import java.util.stream.*;
import java.util.*;
import java.util.Map.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> map = new HashMap();
        for (int i : tangerine){
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        
        List<Entry<Integer,Integer>> entry = map.entrySet()
            .stream().sorted((a,b)->b.getValue() - a.getValue())
            .collect(Collectors.toList());
        
        int cnt = 0;
        for(Entry<Integer,Integer> e : entry){
            cnt += 1;
            k -= e.getValue();
            if (k <= 0) break;
        }
        return cnt;
    }
}
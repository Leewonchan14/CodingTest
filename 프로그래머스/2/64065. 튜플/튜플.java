import java.util.stream.*;
import java.util.*;

class Solution {
    public int[] solution(String s) {
        Map<Integer,Integer> map = new HashMap<>();
        
        String trimmed = s.substring(2, s.length() - 2);
        
        String[] split = trimmed.split("\\},\\{|,");
        
        for (String str : split) {
            int target = Integer.parseInt(str);
            if(!map.containsKey(target)){
                map.put(target,1);
                continue;
            }
            
            map.put(target, map.get(target) + 1);
        }
        
        return map.entrySet().stream()
            .sorted((o1, o2) -> o2.getValue() > o1.getValue() ? 1 : -1) 
            .mapToInt(Map.Entry::getKey).toArray();

    }
}
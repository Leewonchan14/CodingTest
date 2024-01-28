import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String,Integer> map = new HashMap<>();
        
        for(String[] strs: clothes){
            if(!map.containsKey(strs[1])){
                map.put(strs[1], 1);
                continue;
            }
            
            map.put(strs[1],map.get(strs[1]) + 1);
        }
        int mul = 1;
        for(int size : map.values()){
            mul *= (size + 1);
        }
        
        return mul - 1;
    }
}
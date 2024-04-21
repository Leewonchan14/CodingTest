import java.util.*;
class Solution {
    
    public int[] solution(int n) {
        List<Integer> li = new ArrayList();
        for(int i = 0; i <= n; i++){
            if (i % 2 == 1) li.add(i);
        }
        return li.stream().mapToInt(i->(int)i).toArray();
    }
}
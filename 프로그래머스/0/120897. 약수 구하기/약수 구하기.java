import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> rs = new ArrayList();
        for(int i = 1; i <= n; i++){
            if (n % i == 0) rs.add(i);
        }
        return rs.stream().mapToInt(i->(int)i).toArray();
    }
}
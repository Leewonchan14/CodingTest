import java.util.*;
class Solution {
    public int[] solution(int n, int k) {
        List<Integer> rs = new ArrayList();
        for(int i = k; i <= n; i += k){
            rs.add(i);
        }
        return rs.stream().mapToInt(i->(int)i).toArray();
    }
}
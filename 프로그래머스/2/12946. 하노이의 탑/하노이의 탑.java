import java.util.*;
import java.util.stream.*;
class Solution {
    List<int[]> result = new ArrayList();
    public int[][] solution(int n) {
        move(1, 3, 2, n);
        return result.stream().toArray(int[][]::new);
    }
    
    public void move(int start, int end, int other, int cnt){
        if (cnt == 1){
            result.add(new int[] { start, end });
            return ;
        }
        
        move(start, other, end, cnt - 1);
        move(start, end, other, 1);
        move(other, end, start, cnt - 1);
    }
}
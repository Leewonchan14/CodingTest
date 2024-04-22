import java.util.stream.*;
import java.util.*;

class Solution {
    List<Integer> scores = new ArrayList();
    public int solution(int[] cards) {
        boolean[] visited = new boolean[cards.length + 1];
        
        for(int i : cards){
            if (visited[i]) continue;
            int cnt = 0;
            int index = i;
            while (!visited[index]){
                cnt += 1;
                visited[index] = true;
                index = cards[index - 1];
            }
            
            scores.add(cnt);
        }
        
        if (scores.size() == 1) return 0;
        
        int[] arr = scores.stream()
            .sorted(Comparator.comparing((Integer i) -> -(int)i))
            .mapToInt(i->(int)i)
            .toArray();
        
        return arr[0] * arr[1];
    }
}
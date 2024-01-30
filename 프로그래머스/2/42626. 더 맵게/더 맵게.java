import java.util.stream.*;
import java.util.*;
class Solution {
    
    PriorityQueue<Integer> que = new PriorityQueue<>();
    
    public int solution(int[] scoville, int K) {
        for(int i = 0; i < scoville.length; i++){
            que.add(scoville[i]);
        }
        
        int answer = 0;
        int pre;
        do {
            if(que.peek() >= K) return 0;
            if(que.size() < 2) return -1;
            
            pre = que.poll();
            int next = que.poll();
            
            que.add(pre + next * 2);
            answer++;
        } while(que.peek() < K);
        
        return answer;
    }
}
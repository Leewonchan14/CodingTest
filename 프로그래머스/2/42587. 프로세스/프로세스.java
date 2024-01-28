import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new LinkedList<>();
        
        for(int i = 0; i< priorities.length;i++){
            int[] ad = new int[]{i, priorities[i]};
            q.add(ad);
        }
        
        Arrays.sort(priorities);
        int count = 1;
        
        for(int i = priorities.length - 1; i >= 0; i--){
            int[] qInt = q.poll();
            
            while(qInt[1] < priorities[i]){
                q.add(qInt);
                qInt = q.poll();
            }
            if(qInt[0] == location){
                break;
            }
            
            count++;
        }

        return count;
    }
}
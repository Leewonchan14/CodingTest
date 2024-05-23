import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        
        Map<Integer, List<Integer>> dic = new HashMap();
        
        for(int i = 1; i <= n; i++){
            dic.put(i, new ArrayList<>());
        }
            
        for (int[] arrs : roads){
            dic.get(arrs[0]).add(arrs[1]);
            dic.get(arrs[1]).add(arrs[0]);
        }
        
        
        LinkedList<int[]> queue = new LinkedList<>();
        
        int[] dp = new int[n + 1];
        for(int i = 0; i < dp.length; i++){
            dp[i] = -1;
        }
        dp[destination] = 0;
        queue.addLast(new int[]{destination, 0});
        while (!queue.isEmpty()){
            int[] arr = queue.pollFirst();
            
            for(Integer i : dic.get(arr[0])){
                if (dp[i] != -1) continue;
                
                dp[i] = arr[1] + 1;
                queue.addLast(new int[]{i, arr[1] + 1});
            }
            
        }
        
        
        return Arrays.stream(sources).map(i->dp[i]).toArray();
        
        
    }


}
import java.util.stream.*;
import java.util.*;

class Solution {
    public int maxSheep = 0;
    public int[][] child;
    public int[] info;
    
    public int solution(int[] info, int[][] edges) {
        child = new int[info.length][2];
        this.info = info;
        
        for (int[] ab : edges) {
            int idx = 1;
            if (child[ab[0]][0] == 0) {
                idx = 0;
            }
            child[ab[0]][idx] = ab[1];
        }
        
        Set<Integer> set = new HashSet<Integer>();
        set.add(0);
        dfs(1, 0, set);
        return maxSheep;
    }
    
    public void dfs(int sheepCnt, int wolfCnt, Set<Integer> nodes){
        if (wolfCnt >= sheepCnt){
            return;
        }
        
        maxSheep = Math.max(sheepCnt, maxSheep);
        
        for(int node : nodes){
            for(int nextNode : child[node]){
                if (nextNode == -1) continue;
                if (nodes.contains(nextNode)) continue;
                
                Set<Integer> set = new HashSet<>(nodes);
                set.add(nextNode);
                
                if(info[nextNode] == 1){
                    dfs(sheepCnt, wolfCnt + 1, set);
                } else {
                    dfs(sheepCnt + 1, wolfCnt, set);
                }
            }
        }
    }
}
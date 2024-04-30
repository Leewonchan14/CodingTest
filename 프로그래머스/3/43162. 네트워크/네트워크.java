import java.util.stream.*;
import java.util.*;
class Solution {
    boolean[] visited;
    ArrayList<Integer>[] dic;
    public void recursive(int point){
        visited[point] = true;
        for(int n : dic[point]){
            if (visited[n]) continue;
            recursive(n);
        }
    }
    
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        
        dic = new ArrayList[n];
        for (int i = 0; i < n; i++){
            dic[i] = new ArrayList<Integer>();
        }
        
        for(int i = 0; i < computers.length; i++){
            for(int j = 0; j < computers[0].length; j++){
                if (computers[i][j] == 0) continue;
                dic[i].add(j);
                dic[j].add(i);
            }
        }
        int cnt = 0;
        for(int i = 0; i< n; i++){
            if (visited[i]) continue;
            recursive(i); cnt++;
        }
        
        return cnt;
    }
}
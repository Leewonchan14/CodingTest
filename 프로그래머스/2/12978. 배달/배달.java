import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int N, int[][] road, int K) {
        int[] weight = new int[N + 1];
        ArrayList<int[]>[] list = new ArrayList[N + 1];
        for(int i = 0; i < N + 1; i++){
            weight[i] = 2000000000;
            list[i] = new ArrayList<>();
        }
        
        weight[1] = 0;
        
        for(int[] ints : road){
            int a = ints[0];
            int b = ints[1];
            int c = ints[2];
            
            list[a].add(new int[]{c, b});
            list[b].add(new int[]{c, a});
        }
        
        LinkedList<Integer> que = new LinkedList<>();
        
        que.addLast(1);
        
        while (!que.isEmpty()){
            int node = que.pollFirst();
            
            for(int[] nInts : list[node]){
                if (nInts[0] + weight[node] < weight[nInts[1]]){
                    weight[nInts[1]] = nInts[0] + weight[node];
                    que.addLast(nInts[1]);
                }
            }
            
        }
        
        return (int)Arrays.stream(weight).filter(i->i<=K).count();
    }
}
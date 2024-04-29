import java.util.*;
import java.util.stream.*;

class Go{
    public int weight;
    public int n;
    
    public Go(int weight, int n){
        this.weight = weight;
        this.n = n;
    }
    
    public String toString(){
        return  "weight : " + weight + ", n : " + n;
    }
}

class Solution {
    
    List<Go>[] dir;
    int[] weights;
    
    public int daikstra(int K){
        PriorityQueue<Go> que = new PriorityQueue<>((Go g1, Go g2) -> g1.weight - g2.weight);
        
        que.add(new Go(0, 1));
        
        while(!que.isEmpty()){
            Go g = que.poll();
            for(Go ng : dir[g.n]){
                if(ng.weight + g.weight < weights[ng.n]){
                    weights[ng.n] = ng.weight + g.weight;
                    que.add(new Go(weights[ng.n], ng.n));
                }
            }
        }
        
        return (int)Arrays.stream(weights).filter(i->i <= K).count();
    }
    
    
    public int solution(int N, int[][] road, int K) {
        dir = new List[N + 1];
        for (int i = 0; i < N + 1; i++){
            dir[i] = new ArrayList<Go>();
        }
        
        weights = new int[N + 1];
        for(int i = 0 ; i < N + 1; i++){
            weights[i] = 2000000000;
        }
        weights[1] = 0;
        
        for(int[] r : road){
            dir[r[0]].add(new Go(r[2], r[1]));
            dir[r[1]].add(new Go(r[2], r[0]));
        }

        return daikstra(K);
    }
}
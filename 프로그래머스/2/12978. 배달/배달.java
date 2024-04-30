import java.util.*;
import java.util.stream.*;

class Solution {
    public class Node{
        public int weight = 2000000000;
        public List<Edge> edges = new ArrayList<>();
        
        public String toString(){
            return "weight : " + weight;
        }
    }
    
    public class Edge{
        public Node a;
        public Node b;
        public int weight;
        
        public Edge(Node a, Node b, int weight){
            this.a = a;
            this.b = b;
            this.weight = weight;
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        Node[] nodes = new Node[N + 1];
        for(int i = 0 ; i < N + 1 ; i++){
            nodes[i] = new Node();
        }
        
        for(int[] r : road){
            nodes[r[0]].edges.add(new Edge(nodes[r[0]], nodes[r[1]], r[2]));
            nodes[r[1]].edges.add(new Edge(nodes[r[1]], nodes[r[0]], r[2]));
        }
        
        PriorityQueue<Edge> que = new PriorityQueue<>((Edge e1, Edge e2)-> e1.weight - e2.weight);
        
        Node now = nodes[1];
        
        now.weight = 0;
        
        for(Edge e : now.edges){
            que.add(e);
        }
        
        while(!que.isEmpty()){
            Edge e = que.poll();
            if(e.a.weight + e.weight >= e.b.weight) continue;
            
            e.b.weight = e.a.weight + e.weight;
            for(Edge e2 : e.b.edges){
                que.add(e2);
            }
        }
        
        return (int)Arrays.stream(nodes).filter(n -> n.weight <= K).count();
    }
}
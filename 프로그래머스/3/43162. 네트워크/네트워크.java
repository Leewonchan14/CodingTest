import java.util.stream.*;
import java.util.*;

class Solution {
    public class Node{
        boolean isVisited = false;
        List<Node> nodes = new ArrayList<>();
        
        public String toString(){
            return "" + isVisited;
        }
    }
    
    public int solution(int n, int[][] computers) {
        Node[] nodes = new Node[n + 1];
        for(int i = 0; i < n + 1; i++){
            nodes[i] = new Node();
        }
        
        for(int i = 0; i < computers.length; i++){
            for(int j = 0; j <computers[0].length; j++){
                if (computers[i][j] == 0) continue;
                nodes[i + 1].nodes.add(nodes[j + 1]);
                nodes[j + 1].nodes.add(nodes[i + 1]);
            }
        }
        
        LinkedList<Node> que = new LinkedList<>();
        
        int cnt = 0;
        
        for(Node node : nodes){
            if (node.isVisited) continue;
            cnt++;
            que.addLast(node);
            
            while(!que.isEmpty()){
                Node pollNode = que.pollFirst();
                for(Node nearNode : pollNode.nodes){
                    if (nearNode.isVisited) continue;
                    nearNode.isVisited = true;
                    que.addLast(nearNode);
                }
            }
        }
        
        return cnt - 1;
        
        
    }
}
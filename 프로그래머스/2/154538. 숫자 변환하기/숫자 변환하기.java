import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int x, int y, int n) {
        return bfs(x, y, n);
    }
    
    int bfs(int x, int y, int n){
        LinkedList<int[]> list = new LinkedList();
        Set<Integer> visited = new HashSet();
        visited.add(x);
        list.addLast(new int[]{x, 0});
        
        while(!list.isEmpty()){
            int[] nv = list.pollFirst();
            int nx = nv[0];
            int cnt = nv[1];
            
            if(nx == y) return cnt;
            
            for(int ny :getNextY(nx, n)){
                if (ny <= y && !visited.contains(ny)){
                    visited.add(ny);
                    list.addLast(new int[]{ny, cnt + 1});
                }
            }
        }
        
        return -1;
    }
    
    int[] getNextY(int x, int n){
        return new int[]{x + n, x * 2, x * 3};
    }
}
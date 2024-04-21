import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        int[] dy = {0 , -1, 0 , 1};
        int[] dx = {1, 0 , -1 , 0};
        LinkedList<int[]> que = new LinkedList();
        int[] yx = {0,0,0};
        que.addLast(yx);
        while(!que.isEmpty()){
            int[] dot = que.pollFirst();
            if (dot[0] == maps.length - 1 && dot[1] == maps[0].length - 1){
                return dot[2] + 1;
            }
            
            for(int i = 0; i < 4; i++){
                int ny = dot[0] + dy[i];
                int nx = dot[1] + dx[i];
                if(0<= ny && ny < maps.length &&
                   0 <= nx && nx < maps[0].length &&
                   maps[ny][nx] == 1 &&
                   !visited[ny][nx]){
                    visited[ny][nx] = true;
                    que.addLast(new int[] {ny,nx, dot[2] + 1});
                }
                    
                
            }
        }
        
        
        return -1;
    }
}
import java.util.stream.*;
import java.util.*;

class Solution {
    public int[] dy = new int[] {0, -1, 0, 1};
    public int[] dx = new int[] {-1, 0, 1, 0};
    public int[][][] cost;
    
    public boolean isCorner(int preY, int preX, int y, int x, int ny, int nx){
        if(preY == -1 && preX == -1){
            return false;
        }
        
        if ((preY == y && y == ny) || (preX == x && x == nx)){
            return false;
        }
        
        return true;
    }
    
    
    public int bfs(int[][] board){
        LinkedList<int[]> que = new LinkedList<>();
        
        que.add(new int[]{-1,-1, 0, 0, 0});
        
        while(!que.isEmpty()){
            int[] ints = que.pollFirst();
            
            for(int i = 0; i < 4; i++){
                int ny = ints[2] + dy[i];
                int nx = ints[3] + dx[i];
                
                if (ny < 0 || ny >= cost.length || nx < 0 || nx >= cost.length) continue;
                
                if(ints[0] == ny && ints[1] == nx) continue;
                
                if (board[ny][nx] == 1) continue;
                    
                int sum = ints[4] + 100;
                if (isCorner(ints[0], ints[1], ints[2], ints[3], ny, nx)){
                    sum += 500;
                }
                
                if (sum >= cost[ny][nx][i]) continue;
                
                cost[ny][nx][i] = sum;
                que.addLast(new int[]{ints[2], ints[3], ny, nx, sum});
            }
        }
        
        return (int)Arrays.stream(cost[cost.length - 1][cost.length - 1]).min().orElse(0);
    }
    
    
    public int solution(int[][] board) {
        cost = new int[board.length][board.length][4];
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board.length; j++){
                for(int k = 0; k < 4; k ++){
                    cost[i][j][k] = 2000000000;
                }
            }
        }
        
        for(int i = 0; i < 4; i++){
            cost[0][0][i] = 0;
        }
        
        return bfs(board);
    }
}
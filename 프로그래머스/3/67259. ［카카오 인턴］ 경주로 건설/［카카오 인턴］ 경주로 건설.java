import java.util.*;
import java.util.stream.*;

class Solution {
    class Point{
        public int cost;
        public int y;
        public int x;
        public int ny;
        public int nx;
        public int preY;
        public int preX;
        
        public Point(int cost, int y, int x, int ny, int nx, int preY, int preX){
            this.cost = cost;
            this.y = y;
            this.x = x;
            this.ny = ny;
            this.nx = nx;
            this.preY = preY;
            this.preX = preX;
        }
        
        public String toString(){
            return "cost : " + cost;
        }
    }
    
    
    PriorityQueue<Point> que = new PriorityQueue<>((Point p1, Point p2)->p1.cost - p2.cost);
    public int solution(int[][] board) {
        return bfs(board);
    }
    
    public boolean isCorner(int y, int x, int ny, int nx, int preY, int preX){
        if (y == 0 && x == 0){
            return false;
        }

        return !((y - preY == ny - y) && (x - preX == nx - x));
    }
    
    
    public int bfs(int[][] board){
        int length = board.length;
        int[][][] visited = new int[length][length][4];
        
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                for (int k = 0; k < 4; k++) {
                    visited[i][j][k] = 1000000000;
                }
            }
        }
        
        int[] dy = new int[]{0, -1, 0, 1};
        int[] dx = new int[]{-1, 0, 1, 0};
        
        que.add(new Point(0,0,0,0,0,0,0));
        for(int i = 0; i < 4; i++){
            visited[0][0][i] = 0;
        }
        
        while(!que.isEmpty()){
            Point p = que.poll();
            
            for(int i = 0; i < 4; i++){
                int ny = p.y + dy[i];
                int nx = p.x + dx[i];
                    
                if (0 <= ny && ny < length && 0 <= nx && nx < length){
                    if( board[ny][nx] == 1 ){
                        continue;
                    }
                    
                    int n_cost = p.cost + 100;
                    
                    Point newPoint = new Point(0, ny, nx, ny, nx, p.y, p.x);
                    if (isCorner(p.y, p.x, ny, nx, p.preY, p.preX)){
                        n_cost += 500;
                    }
                    
                    if(n_cost > visited[ny][nx][i]){
                        continue;
                    }
                    
                    newPoint.cost = n_cost;
                    
                    visited[ny][nx][i] = n_cost;
                    que.add(newPoint);
                }
                
            }
                
        }
        int[] last = visited[length - 1][length - 1];
        return Math.min(Math.min(last[2], last[3]), Math.min(last[0], last[1]));
        
    }
}
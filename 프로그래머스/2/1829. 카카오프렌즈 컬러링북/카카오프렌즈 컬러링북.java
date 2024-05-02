import java.util.stream.*;
import java.util.*;

class Solution {
    int[] dy = {1,0,-1,0};
    int[] dx = {0,-1,0,1};
    int M;
    int N;
    int[][] visited;
    LinkedList<int[]> que = new LinkedList<>();
    
    public int dfs(int[] point, int[][] picture){
        if(visited[point[0]][point[1]] == 1) return 0;
        
        int target = picture[point[0]][point[1]];
        
        que.addLast(point);
        visited[point[0]][point[1]] = 1;
        int cnt = 0;
        while(!que.isEmpty()){
            int[] nPoint = que.pollFirst();
            cnt++;
            
            for(int i = 0; i < 4; i++){
                int ny = nPoint[0] + dy[i];
                int nx = nPoint[1] + dx[i];
                
                if (ny < 0 || ny >= M || nx < 0 || nx >= N) continue;
                if (picture[ny][nx] == 0 || picture[ny][nx] != target) continue;
                if (visited[ny][nx] == 1) continue;
                
                visited[ny][nx] = 1;
                que.addLast(new int[]{ny, nx});
            }
        }
        
        return cnt;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        visited = new int[m][n];
        M = m;
        N = n;
        int cnt = 0;
        int max = 0;
        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                if(visited[r][c] == 0 && picture[r][c] != 0){
                    cnt++;
                    max = Math.max(dfs(new int[]{r, c}, picture), max);
                }
            }
        }
        
        return new int[]{cnt, max};
    }
}
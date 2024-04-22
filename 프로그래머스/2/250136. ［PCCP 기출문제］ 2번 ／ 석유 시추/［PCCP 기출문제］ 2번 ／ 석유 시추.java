import java.util.stream.*;
import java.util.*;

class Solution {
    int[] dy = new int[] {0, -1, 0, 1};
    int[] dx = new int[] {-1, 0, 1, 0};
    int[] columns;
    public int bfs(int[][] land, int y, int x){
        LinkedList<int[]> que = new LinkedList();
        Set<Integer> set = new HashSet();
        que.addLast(new int[]{y, x});
        land[y][x] = 0;
        int cnt = 0;
        while(!que.isEmpty()){
            int[] pop = que.pollLast();
            set.add(pop[1]);
            cnt++;
            for(int i = 0; i < 4; i++){
                int ny = pop[0] + dy[i];
                int nx = pop[1] + dx[i];
                if(ny < 0 || nx < 0 || ny >= land.length || nx >= land[0].length) continue;
                if (land[ny][nx] == 0) continue;
                
                land[ny][nx] = 0;
                que.addLast(new int[] {ny, nx});
            }
        }
        
        for(Integer i : set){
            columns[i] += cnt;
        }
        
        return cnt;
    }
    
    public int solution(int[][] land) {
        List<Integer> sumList = new ArrayList();
        
        columns = new int[land[0].length];
        
        for (int c = 0; c < land[0].length; c++){
            for(int r = 0; r < land.length ; r++){
                if (land[r][c] == 1)
                    bfs(land, r, c);
            }
        }
        
        int[] arr = Arrays.stream(columns).boxed()
            .sorted(
            Comparator.comparing((Integer i) -> -(int)i)
        ).mapToInt(i->(int)i).toArray();
        
        return arr[0];
    }
}
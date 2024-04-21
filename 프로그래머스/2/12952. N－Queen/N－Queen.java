import java.util.*;
class Solution {
    int[] r_visited;
    int[] c_visited;
    int N = 0;
    Set<Integer> y_ = new HashSet();
    Set<Integer> _y = new HashSet();
    int cnt = 0;
    public int solution(int n) {
        N = n;
        r_visited = new int[n];
        c_visited = new int[n];

        track(0);
        
        return cnt;
    }
    
    public int track(int count){
        if (count == N) {
            cnt+= 1;
            return 0;
        }
        int r = count;
        for(int c = 0; c < N; c++){
            if (c_visited[c] == 1) continue;
            if(!y_.contains(r + c) && !_y.contains(r - c)){
                r_visited[r] = 1;
                c_visited[c] = 1;
                y_.add(r + c);
                _y.add(r - c);

                track(count + 1);

                r_visited[r] = 0;
                c_visited[c] = 0;
                y_.remove(r + c);
                _y.remove(r - c);
            }
        }
        
        return 0;
    }
}
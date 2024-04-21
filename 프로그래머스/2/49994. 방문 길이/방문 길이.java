import java.util.*;

class Solution {
    public int solution(String dirs) {
        Map<String, int[]> map = new HashMap();
        Set<Integer> visited = new HashSet();
        map.put("U", new int[]{1, 0});
        map.put("D", new int[]{-1, 0});
        map.put("L", new int[]{0, -1});
        map.put("R", new int[]{0, 1});
        int[] point = new int[]{0,0};
        int cnt = 0;
        for(String s : dirs.split("")) {
            double ny = point[0] + map.get(s)[0];
            double nx = point[1] + map.get(s)[1]; 
                
            if (!(-5 <= ny && ny <= 5 && -5 <= nx && nx <= 5)) continue;
            
            double[] isGo = new double[] {(point[0] + ny) / 2, (point[1] + nx) / 2};
            int hash = Objects.hash("" + isGo[0] + isGo[1]);
            if (!visited.contains(hash)) cnt += 1;
            
            visited.add(hash);
            point[0] = (int)ny;
            point[1] = (int)nx;
        }
        
        return cnt;
    }
}
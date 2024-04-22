import java.util.stream.*;
import java.util.*;

class Point{
    int start;
    int end;
    
    public Point(int start, int end){
        this.start = start;
        this.end = end;
    }
    
    @Override
    public String toString(){
        return "[" + start + ", " + end + "]";
    }
    
    public int gap(){
        return end - start;
    }
}

class Solution {
    public int solution(int[][] targets) {
        List<Point> li = Arrays.stream(targets)
            .map(i-> new Point(i[0],i[1]))
            .sorted(
                Comparator.comparing((Point i)->i.end)
                .thenComparing(Point::gap)
           )
            .collect(Collectors.toList());
        
        double shoot = 0;
        // System.out.println(li);
        
        Iterator<Point> iter = li.iterator();
        
        int cnt = 0;
        
        while(iter.hasNext()){
            Point p = iter.next();
            
            if (p.start < shoot && shoot < p.end) continue;
            
            shoot = p.end - 0.5;
            cnt += 1;
        }
        
        return cnt;
    }
}
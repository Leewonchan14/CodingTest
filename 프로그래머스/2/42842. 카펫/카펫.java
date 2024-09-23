import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        for(int h = 1; h <= Math.sqrt(yellow); h++){
            float w1 = yellow / (float)h;
            int w2 = yellow / h;
            
            if (w1 != w2) continue;
                
            if (w2 * 2 + h * 2 + 4 == brown){
                return new int[]{w2 + 2, h + 2};
            }
        }
        
        return null;
    }
}
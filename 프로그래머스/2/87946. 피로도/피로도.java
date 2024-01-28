import java.util.stream.*;
import java.util.*;

class Solution {
    
    int maxCount = 0;

    public int solution(int k, int[][] dungeons) {
        
        boolean[] isGo = new boolean[dungeons.length];
        Go(dungeons, k, 0, isGo);
        
        return maxCount;
    }
    
    public void Go(int[][] dun, int nowFiro, int moveCount, boolean[] isGo){
        
        for(int index = 0; index<isGo.length; index++){
            if(
                !isGo[index] &&
                nowFiro >= dun[index][0] &&
                nowFiro >= dun[index][1]
            ){
                boolean[] isGo2 = isGo.clone();
                isGo2[index] = true;
                Go(dun, nowFiro - dun[index][1],moveCount +1,  isGo2);
            }
            
            if(maxCount < moveCount){
                maxCount = moveCount;
            }
        }
    }
}
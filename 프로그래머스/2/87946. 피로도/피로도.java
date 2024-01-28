import java.util.stream.*;
import java.util.*;

class Solution {
    
    int maxCount = 0;
    boolean[] isGo;
    int[][] dun;

    public int solution(int k, int[][] dungeons) {
        dun = dungeons;
        
        isGo = new boolean[dungeons.length];
        
        Go(k, 0);
        
        return maxCount;
    }
    
    public void Go(int nowFiro, int moveCount){
        for(int index = 0; index<isGo.length; index++){
            // 갈수 있으면
            if(!isGo[index] && nowFiro >= dun[index][0]){
                isGo[index] = true;
                Go(nowFiro - dun[index][1],moveCount +1);
                isGo[index] = false;
            }
            
            if(maxCount < moveCount){
                maxCount = moveCount;
            }
        }
    }
}
import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        boolean[] isSo = new boolean[yellow + 1];
        Arrays.fill(isSo,true);
        
        for(int i = 1; i * i <= yellow; i++){
            // 
            if(yellow % i != 0){
                continue;
            } 
            
            int row = i;
            int col = yellow / i;
            
            if(2*row + 2*col + 4 == brown){
                return new int[]{(row<col ? col:row) + 2, (row<col ? row:col) + 2};
            }
        }
        
        return null;
    }
}
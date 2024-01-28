import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int[] citations) {
        
        Arrays.sort(citations);
        
        int count = 0;
        for(int i = citations.length - 1; citations[i] > count; i-- ){
            count++;
            if(i == 0) break;
        }
        
        return count;
    }
}
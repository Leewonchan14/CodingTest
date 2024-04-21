import java.util.*;

class Solution {
    int[] counts = new int[300];
    public int solution(int[] people, int limit) {
        int max = 0;
        int min = 300;
        for(int weight : people){
            counts[weight]++;
            if (weight > max) max = weight;
            if (weight < min) min = weight;
        }
        
        int[] boat = new int[2];
        int cnt = 0;
        while(true){
            cnt += 1;
                
            if (max + min <= limit && !(min == max && counts[min] <= 1)){
                counts[max] -= 1;
                counts[min] -= 1;
            } else {
                counts[max] -= 1;
            }
            
            while(0 <= max && counts[max] == 0){
                max -= 1;
            }
            while(min < 300 && counts[min] == 0){
                min += 1;
            }
            if (max == -1 || min == 300) break;
            
            if(min == max && counts[max] == 0){
                break;
            }
        }
        
        return cnt;
    }
}
import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        LinkedList<String> cach = new LinkedList<>();
        
        int execTime = 0;
        
        for(String str : cities){
            str = str.toLowerCase();
            boolean isExist = cach.contains(str);
            
            if(isExist){
                cach.remove(str);
                cach.addLast(str);
                
                execTime += 1;
                continue;
            }
            
            if(cacheSize == 0){
                execTime += 5;
                continue;
            }
            
            
            if(cach.size() >= cacheSize){
                cach.pollFirst();
            }
            
            cach.addLast(str);
            
            execTime += 5;
        }
        return execTime;
    }
}
import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int n) {
        
        String binaryString = Integer.toBinaryString(n);
        int oneCount = binaryString.replace("0","").length();
        
        while(true){
            binaryString = Integer.toBinaryString(n + 1);
        
            int nextOneCount = binaryString.replace("0","").length();
            
            if(oneCount == nextOneCount){
                return n + 1;
            }
            n++;
        }
        
    }
}
import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;

        char[] chars = Integer.toBinaryString(n).toCharArray();
        
        for(int i = 0; i<chars.length; i++){
            if(chars[i] == '1'){
                ans++;
                continue;
            }
        }
            
        return ans;
    }
}
import java.util.stream.*;
import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long[] dp1 = new long[sequence.length];
        long[] dp2 = new long[sequence.length];
        for(int i = 0; i < sequence.length; i++){
            dp1[i] = (i % 2 == 0 ? 1 : -1) * sequence[i];
            dp2[i] = (i % 2 == 0 ? -1 : 1) * sequence[i];
        }
        
        for(int i = 1; i < sequence.length; i++){
            dp1[i] = Math.max(dp1[i - 1] + dp1[i], dp1[i]);
            dp2[i] = Math.max(dp2[i - 1] + dp2[i], dp2[i]);
        }
        
        Arrays.sort(dp1);
        Arrays.sort(dp2);
        
        return Math.max(dp1[dp1.length - 1], dp2[dp2.length - 1]);
    }
}
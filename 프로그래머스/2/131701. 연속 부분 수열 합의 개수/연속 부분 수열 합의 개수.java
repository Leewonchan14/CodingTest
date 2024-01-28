import java.util.stream.*;
import java.util.*;
class Solution {
    int[] arr;
    
    int[][] dp;
    public int solution(int[] elements) {
        arr = elements;
        dp = new int[1001][1001];
        // arr = new int[]{1,2,3,4};
        Set<Integer> set = new HashSet<>();
        for(int i = 1; i <= arr.length; i++){
            for(int j = 0; j < arr.length; j++){
                set.add(getInt(j, i));
            }
        }
        
        return set.size();
    }
    
    public int getInt(int n, int len){
        dp[n][len] = dp[n][len - 1]
            + arr[(n + len) % arr.length];
        
        return dp[n][len];
    }
}
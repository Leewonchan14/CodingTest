class Solution {
    int maxScore = 0;
    long[][] dp;
    long solution(int[][] land) {
        dp = new long[land.length + 1][4];
        
        dp[0][0] = land[0][0];
        dp[0][1] = land[0][1];
        dp[0][2] = land[0][2];
        dp[0][3] = land[0][3];
        
        for(int row = 1; row <land.length ; row++){
            for(int col = 0; col < 4; col++){
                long max = 0;
                for(int i = 0; i<4;i++){
                    if(col == i) continue;
                    
                    if(max < dp[row-1][i])
                        max = dp[row-1][i];
                }
                dp[row][col] = max + land[row][col];
            }
        }
        
        long max = 0;
        for(int i = 0; i<4; i++){
            if(max < dp[land.length-1][i])
                max = dp[land.length-1][i];
        }
        
        return max;
    }
}
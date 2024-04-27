// maxv = [-1]
// ls = []
// length = [0]


// def left(v):
//     return (length[0] + v - 1) % length[0]


// def right(v):
//     return (v + 1) % length[0]


// def solution(sticker):
//     length[0] = len(sticker)
//     if length[0] == 1:
//         return sticker[0]

//     dp0 = sticker[:]
//     dp0[1] = dp0[0]
//     dp0[-1] = 0
//     for i in range(2, length[0]):
//         dp0[i] = max(dp0[i - 1], dp0[i - 2] + dp0[i])

//     dp1 = sticker[:]

//     dp1[0] = 0
//     for i in range(2, length[0]):
//         dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

//     return max(dp0[-1], dp1[-1])


// # print(solution(	[14, 6, 5, 11, 3, 9, 2, 10]))

import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        int[] dp1 = new int[sticker.length];
        int[] dp2 = new int[sticker.length];
        
        if (sticker.length == 1){
            return sticker[0];
        }
        
        
        dp1[0] = sticker[0];
        dp1[1] = sticker[0];
        
        int a = 0;
        
        for (int i = 2; i < sticker.length; i++){
            if (i == sticker.length - 1){
                a = dp1[i - 1];
                
            }
            dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
        }
        
        dp2[0] = 0;
        dp2[1] = sticker[1];
        
        for(int i = 2; i < sticker.length; i++){
            dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
        }
        
        return Math.max(a, dp2[sticker.length - 1]);
        
    }
}
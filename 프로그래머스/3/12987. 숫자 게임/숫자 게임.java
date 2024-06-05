import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int aI = 0;
        int bI = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        int cnt = 0;
        while (aI < A.length && bI < B.length){
            if(A[aI] < B[bI]){
                aI++;
                bI++;
                cnt++;
            } else {
                bI++;
            }
        }
        
        return cnt;
    }
}
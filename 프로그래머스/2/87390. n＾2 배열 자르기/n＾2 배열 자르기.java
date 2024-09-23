import java.util.Arrays;
class Solution {
    public static int[] solution(int n, long left, long right) {
        int[] result = new int[(int)(right - left) + 1];
        int idx = 0;
        
        for(long i = left; i < right + 1; i++){
            result[idx++] = (int)Math.max(i % n, i / n) + 1;
        }
        
        return result;
    }
}
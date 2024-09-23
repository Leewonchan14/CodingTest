import java.util.Arrays;
class Solution {
    public static int[] solution(int n, long left, long right) {
        int[] result = new int[(int)(right - left) + 1];
        int idx = 0;
        
        for(long i = left; i < right + 1; i++){
            long w = i % n;
            long h = i / n;
            
            long temp = 0;
            
            if (w <= h) temp = h;
            else temp = w;
            
            result[idx++] = (int)temp + 1;
        }
        
        return result;
    }
}
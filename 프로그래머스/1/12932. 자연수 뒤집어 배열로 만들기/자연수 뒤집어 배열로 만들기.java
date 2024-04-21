import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        int[] chars = str.chars().toArray();
        int[] rs = new int[chars.length];
        for(int i = 0; i < chars.length; i++){
            rs[i] = chars[chars.length - 1 - i] - '0';
        }
        return rs;
    }
}
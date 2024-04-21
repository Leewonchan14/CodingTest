import java.util.stream.*;
import java.util.*;
class Solution {
    public long solution(long n) {
        int[] ints = String.valueOf(n).chars().boxed().sorted((a,b)->b - a).mapToInt(i->(int)i).toArray();
        char[] chars = new char[ints.length];
        for(int i = 0; i < ints.length; i++){
            chars[i] = (char)(ints[i]);
        }
        
        return Long.parseLong(String.valueOf(chars));
    }
}
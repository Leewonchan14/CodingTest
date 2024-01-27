import java.util.stream.*;
import java.util.*;
class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        int max = Arrays.stream(arr).mapToInt(Integer::parseInt).sorted().skip(arr.length - 1).sum();
        int min = Arrays.stream(arr).mapToInt(Integer::parseInt).sorted().limit(1).sum();
        return "" + min + " " + max;
    }
}
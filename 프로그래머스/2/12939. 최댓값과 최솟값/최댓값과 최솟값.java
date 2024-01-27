import java.util.stream.*;
import java.util.*;
class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        int[] arr2 = Arrays.stream(arr).mapToInt(Integer::parseInt).sorted().toArray();
        return arr2[0] + " " + arr2[arr.length-1];
    }
}
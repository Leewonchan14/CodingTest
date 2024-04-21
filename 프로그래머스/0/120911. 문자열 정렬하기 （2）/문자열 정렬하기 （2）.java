import java.util.*;
class Solution {
    public String solution(String my_string) {
        List<Integer> rs = new ArrayList();
        for(int i : my_string.chars().toArray()){
            if('A' <= (char)i  && (char)i <= 'Z'){
                rs.add(i + ('a' - 'A'));
            } else{
                rs.add(i);
            }
        }
        int[] sorted = rs.stream().sorted().mapToInt(i->(int)i).toArray();
        char[] chars = new char[sorted.length];
        for(int i = 0; i < sorted.length; i++){
            chars[i] = (char)sorted[i];
        }
        return String.valueOf(chars);
    }
}
import java.util.*;
class Solution {
    Set<Integer> set = new HashSet();
    public int solution(int[] elements) {
        for(int size = 1; size < elements.length; size++){
            for(int i = 0; i < elements.length; i++){
                int sum = 0;
                for(int j = i; j < i + size; j++){
                    sum += elements[j % elements.length];
                }
                set.add(sum);
            }
        }
        
        int sumv = 0;
        for(int i = 0; i < elements.length; i++){
            sumv += elements[i];
        }
        set.add(sumv);
        return set.size();
    }
}
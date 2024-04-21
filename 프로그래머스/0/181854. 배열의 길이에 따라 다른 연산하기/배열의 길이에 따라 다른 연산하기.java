import java.util.*;
class Solution {
    List<Integer> rs = new ArrayList();
    public int[] solution(int[] arr, int n) {
        for (int i = 0; i < arr.length ; i++){
            if(arr.length % 2 == 1 && i % 2 == 0){
                rs.add(arr[i] + n);
            } else if (arr.length % 2 == 0 && i % 2 == 1){
                rs.add(arr[i] + n);
            }else{
                rs.add(arr[i]);
            }
        }
        
        return rs.stream().mapToInt(i->(int)i).toArray();
    }
}
import java.util.*;
import java.util.stream.*;
class Solution {
    public double[] solution(int k, int[][] ranges) {
        LinkedList<Integer> dp = new LinkedList<>();
        
        dp.addLast(0);
        
        while(k != 1){
            int n_k = 0;
            if (k % 2 == 0){
                n_k = k / 2;
            }else{
                n_k = k * 3 + 1;
            }
            dp.addLast(dp.peekLast() + n_k + k);
            k = n_k;
        }
        
        final int n = dp.size() - 1;
        
        return Arrays.stream(ranges).mapToDouble((int[] ints)->{
            int a = ints[0];
            int b = n + ints[1];
            if (a > n || b > n || b < a){
                return -1;
            }
            return (dp.get(b) - dp.get(a)) / 2.0;
        }).toArray();
    }
}
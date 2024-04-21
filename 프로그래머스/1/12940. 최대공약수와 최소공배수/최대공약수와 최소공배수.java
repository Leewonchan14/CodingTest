import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int n, int m) {
        int min = m < n ? m : n;
        int max = m < n ? n : m;
        int i = min;
        List<Integer> li = new ArrayList();
        while(i >= 1 && !(n % i == 0 && m % i == 0)){
            i--;
        }
        
        int gcd = i;
        
        i = max;
        while(i <= n * m && !(i % n == 0 && i % m == 0)){
            i++;
        }
        int mc = i;
        int[] rs = {gcd, mc};
        return rs;
    }
}
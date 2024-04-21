import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        LinkedList<int[]> stk = new LinkedList();
        int[] rs = new int[prices.length];
        for(int i = 0; i < prices.length; i++){
            if(stk.isEmpty() || stk.peekLast()[1] <= prices[i]){
                stk.addLast(new int[]{i, prices[i]});
                continue;
            }
            while(!stk.isEmpty() && stk.peekLast()[1] > prices[i]){
                int[] pop = stk.pollLast();
                rs[pop[0]] = i - pop[0];
            }
            
            stk.addLast(new int[] {i, prices[i]});
        }
        
        int k = prices.length - 1;
        while(!stk.isEmpty()){
            int[] pop = stk.pollLast();
            rs[pop[0]] = k - pop[0];
        }
        
        return rs;
    }
}
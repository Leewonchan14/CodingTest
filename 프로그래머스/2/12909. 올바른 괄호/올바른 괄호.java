import java.util.*;
class Solution {
    boolean solution(String str) {
        LinkedList<Integer> st = new LinkedList();
        for(int s : str.chars().toArray()){
            if(st.isEmpty() && s ==')' ) return false;
            
            if (st.isEmpty() || s == '('){
                st.addLast(s);
                continue;
            }
            
            if(st.peekLast() == '('){
                st.pollLast();
            } else{
                return false;
            }
        }
        
        return st.isEmpty();
    }
}
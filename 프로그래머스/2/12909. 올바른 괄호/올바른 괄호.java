import java.util.stream.*;
import java.util.*;
class Solution {
    boolean solution(String s1) {
        
        char[] s = s1.toCharArray();
        
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < s.length; i++){
            // if open add
            if(s[i] == '('){
                stack.add((int)s[i]);
            }
            
            // if close check
            if(s[i] == ')'){
                if(stack.isEmpty())
                    return false;
                
                if (stack.pop() != '('){
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}
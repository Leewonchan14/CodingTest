import java.util.stream.*;
import java.util.*;
class Solution
{
    public int solution(String s)
    {
        Stack<Integer> stack = new Stack();
        char[] chars = s.toCharArray();
        
        for(int i = 0; i < chars.length;i++){
            if(stack.isEmpty()){
                stack.add((int)chars[i]);
                continue;
            }
            
            if(chars[i] == stack.peek()){
                stack.pop();
                continue;
            }
            
            stack.add((int)chars[i]);
        }
        
        return stack.isEmpty() ? 1 : 0;
    }
}
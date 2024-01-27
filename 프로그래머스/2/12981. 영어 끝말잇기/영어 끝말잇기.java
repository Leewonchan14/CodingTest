import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        List<List<String>> ll = new ArrayList<>();
        
        for(int i = 0; i < n ; i++){
            ll.add(new ArrayList<String>());
        }
    
        Stack<String> preWords = new Stack<>();

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다. 
        // System.out.println(ll[0]);
        
        
        for(int i = 0; i< words.length ; i++){
            int nowNum = i % n;
            
            boolean isPre = preWords.contains(words[i]);
            
            if(preWords.isEmpty()){
                ll.get(nowNum).add(words[i]);
                preWords.add(words[i]);
                continue;
            }
                
            
            if(
                isPre || 
                preWords.peek().charAt(preWords.peek().length() - 1) != words[i].charAt(0)
            ){
                return new int[]{nowNum + 1, ll.get(nowNum).size() + 1};
            }
            
            ll.get(nowNum).add(words[i]);
            preWords.add(words[i]);
        }

        return new int[]{0,0};
    }
}
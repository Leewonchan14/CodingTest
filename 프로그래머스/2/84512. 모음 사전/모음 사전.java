class Solution {
    String[] str = "A E I O U".split(" ");
    int cnt = 0;
    String target;
    public int solution(String word) {
        target = word;
        
        track("");
        
        
        return cnt;
    }
    
    public boolean track(String input){
        if (input.equals(target)) {
            return true;
        }
            
        
        if (input.length() == 5) {
            return false;
        }
        
        for(String s: str){
            boolean good = track(input + s);
            cnt += 1;
            if(good){
              return true;  
            }
        }
        
        return false;
    }
}
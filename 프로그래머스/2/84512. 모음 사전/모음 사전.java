class Solution {
    String[] arr = "A E I O U".split(" ");
    int count = 0;
    String target;
    public int solution(String word) {
        target = word;
        
        dfs("");
        
        return count;
    }
    
    public int dfs(String input){
        if(input.equals(target)){
            return 1;
        }
        
        if(input.length() == 5){
            return 0;
        }
        
        for(String str : arr){
            count++;
            if(dfs(input+str) == 1){
                return 1;
            }
        }
        
        return 0;
    }
}
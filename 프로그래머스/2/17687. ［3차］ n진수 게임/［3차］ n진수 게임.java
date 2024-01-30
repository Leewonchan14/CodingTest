class Solution {
    public String solution(int n, int t, int m, int p) {
        String sumStr = "";
        int count = 0;
        int index = 0;
        while(t > 0){
            
            String toStr = Integer.toString(count++ ,n).toUpperCase();
            
            for(int i = 0;i < toStr.length();i++){
                if(((index + i) % m + 1) == p ){
                    sumStr += toStr.substring(i,i+1);
                    t--;
                    if(t <= 0) break;
                }
            }
            
            index += toStr.length();
        }
        
        return sumStr;
    }
}
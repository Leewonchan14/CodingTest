class Solution {
    public String solution(String st) {
        String[] strs = st.split(" ");
        int max = Integer.parseInt(strs[0]);
        int min = Integer.parseInt(strs[0]);
        for(String s : strs){
            int target = Integer.parseInt(s);
            if (target > max){
                max = target;
            }
            if (target < min){
                min = target;
            }
        }
        
        return min + " " + max;
        
    }
}
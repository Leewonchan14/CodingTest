class Solution {
    public String solution(String my_string, String alp) {
        char target = alp.charAt(0);
        String rs = "";
        for(int i = 0 ; i < my_string.length(); i++){
            char c = my_string.charAt(i);
            if (target == c) rs += String.valueOf((char)(target + ('A' - 'a')));
            else rs += String.valueOf(c);
        }
        return rs;
    }
}
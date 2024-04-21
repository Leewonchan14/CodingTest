class Solution {
    public String solution(String my_string) {
        int[] str = my_string.chars().toArray();
        char[] rs = new char[my_string.length()];
        for (int i=0; i< my_string.length(); i++){
            rs[i] = (char)str[str.length - 1 - i];
        }
        return String.valueOf(rs);
    }
}
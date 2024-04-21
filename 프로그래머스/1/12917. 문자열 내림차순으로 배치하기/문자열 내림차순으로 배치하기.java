class Solution {
    public String solution(String s) {
        int[] ints = s.chars().boxed().sorted((a,b)->b-a).mapToInt(i->(int)i).toArray();
        char[] chars = new char[ints.length];
        for(int i = 0; i<ints.length;i++){
            chars[i] = (char)ints[i];
        }
        return String.valueOf(chars);
    }
}
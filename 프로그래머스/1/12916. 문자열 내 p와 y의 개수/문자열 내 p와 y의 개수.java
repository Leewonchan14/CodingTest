class Solution {
    boolean solution(String s) {
        int y_c = 0;
        int p_c = 0;
        for (int i : s.chars().toArray()){
            if(i == 'P' || i == 'p') p_c += 1;
            if(i == 'Y' || i == 'y') y_c += 1;
        }
        return y_c == p_c;

    }
}
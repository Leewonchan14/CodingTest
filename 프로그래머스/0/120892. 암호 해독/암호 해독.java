import java.util.*;
class Solution {
    public String solution(String cipher, int code) {
        List<String> strs = new ArrayList();
        for(int i = 0; i < cipher.length(); i++){
            if((i + 1) % code == 0) strs.add(String.valueOf(cipher.charAt(i)));
        }
        return String.join("", strs);
    }
}
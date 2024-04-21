import java.util.*;
class Solution {
    public String solution(String my_string) {
        List<String> li = new ArrayList();
        int[] chars = my_string.chars().toArray();
        for(int s : chars){
            String item = String.valueOf((char)s);
            if ("aeiou".contains(item)){
                continue;
            }
            li.add(item);
        }
        return String.join("",li);
    }
}
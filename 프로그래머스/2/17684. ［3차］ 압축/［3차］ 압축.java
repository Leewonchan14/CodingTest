import java.util.stream.*;
import java.util.*;
class Solution {
    
    Map<String, Integer> map;
    List<Integer> list = new ArrayList<>();
    int DicIndex = 1;
    
    public int[] solution(String msg) {
        init();

        for(int i = 0; i< msg.length();){

            int j = i + 1;
            String now = "";
            String next = msg.substring(i, j);;

            // next 가 map에 없을때까지
            while (map.containsKey(next)) {
                now = next;
                j++;
                if(j > msg.length()){
                    break;
                }
                next = msg.substring(i, j);
            }
            // next가 이제 map에 없다면
            list.add(map.get(now));
            put(next);
            i = j - 1;
        }

        return list.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public void init(){
        map = new HashMap<>();
        
        for(char c = 'A'; c <= 'Z' ; c++){
            map.put(String.valueOf(c), DicIndex);
            DicIndex++;
        }
    }
    
    public void put(String input){
        map.put(input, DicIndex++);
    }
}
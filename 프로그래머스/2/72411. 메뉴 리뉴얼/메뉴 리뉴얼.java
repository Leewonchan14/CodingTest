import java.util.*;
import java.util.stream.*;


class Solution {
    List<String> result = new ArrayList();
    LinkedList<Integer> ls;
    Map<String, Integer> map;
    
    void Dfs(String[] n_order, int k){
        if (ls.size() == k){
            int[] ints = ls.stream().mapToInt(i -> n_order[i].charAt(0)).toArray();
            char[] chars = new char[ints.length];
            for (int i = 0; i < ints.length; i++){
                chars[i] = (char)ints[i];
            }
            
            String sub = String.valueOf(chars);
            int cnt = map.getOrDefault(sub, 0) + 1;
            map.put(sub, cnt);
            return;
        }
        
        for (int i = 0; i < n_order.length; i++){
            if (ls.size() == 0 || ls.peekLast() < i){
                ls.addLast(i);
                Dfs(n_order, k);
                ls.pollLast();
            }
        }
    }
    
    
    
    public String[] solution(String[] orders, int[] course) {
        
        for(int size : course){
            map = new HashMap();
            for(String order : orders){
                String[] n_order = Arrays.stream(order.split("")).sorted().toArray(String[]::new);
                ls = new LinkedList();
                Dfs(n_order ,size);                
            }
            
            if (map.isEmpty()) continue;
            
            int maxv = map.values().stream().mapToInt(i->(int)i).max().orElse(0);
            final int max = Math.max(maxv, 2);
            List<String> list = map.entrySet().stream()
                .filter(entry -> entry.getValue() >= max)
                .map(entry -> entry.getKey())
                .collect(Collectors.toList());
            
            for(String s : list){
                result.add(s);
            }
        }
        
        return result.stream().sorted().toArray(String[]::new);
    }
}